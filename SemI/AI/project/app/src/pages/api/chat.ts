import { v4 as uuid } from 'uuid';
import dialogflow from '@google-cloud/dialogflow';
import type { NextApiRequest, NextApiResponse } from 'next'
import { Configuration, OpenAIApi } from 'openai';

type Data = {
  name: string
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  const { query } = req.body;

   const configuration = new Configuration({
    apiKey: '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'
  });

  const openai = new OpenAIApi(configuration);

  const sessionId = uuid();

  const sessionClient = new dialogflow.SessionsClient();
  const sessionPath = sessionClient.projectAgentSessionPath(
    'sudipto-test-project',
    sessionId
  );

  if (!query) {
    res.status(200).json({ answer: 'Sorry, I could not understand that.' })
    return;
  }

  const request = {
    session: sessionPath,
    queryInput: {
      text: {
        text: query,
        languageCode: 'en-IN',
      },
    },
  };

  const responses = await sessionClient.detectIntent(request);
  const result = responses[0].queryResult;

  if (query == 'get all data in kg') {
    fetch('http://localhost:9999/blazegraph/sparql?query=select%20*%20where%20%7B%3Fs%20%3Fp%20%3Fo%7D%20limit%2010&format=json')
    .then(res => res.json())
    .then(json =>  res.status(200).json({ answer: JSON.stringify(json.results.bindings) }))
    .catch(err => console.error('error:' + err));
    
   return;
  }

  if (query == 'get a case from 1977') {
    fetch('http://localhost:9999/blazegraph/sparql?query=prefix%20nyon:%20%3Chttps://w3id.org/def/NyOnLegalOntology%23%3E%0Aprefix%20:%20%3Chttps://cs.du.ac.in/kg/sudipto%23%3Eselect * where { ?case nyon:date ?d ; nyon:hasCaseName ?n . filter(regex(?d, \"1977\")) }&format=json')
    .then(res => res.json())
.then(async json => {
      let ans = JSON.stringify(json.results.bindings);
      ans = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: `use the following json from sparql query response to construct a natural langiage answer: ${ans}`,
        temperature: 0,
        max_tokens: 200,
      });
      res.status(200).json({ answer: ans.data.choices[0].text || 'Sorry, I could not understand that.' });
    })
      .catch(err => console.error('error:' + err));
    
   return;
  }

  if (query == 'get case name whose judgement whose author\'s name is justice y chandrachud') {
    fetch('http://localhost:9999/blazegraph/sparql?query=prefix%20nyon:%20%3Chttps://w3id.org/def/NyOnLegalOntology%23%3E%0Aprefix%20:%20%3Chttps://cs.du.ac.in/kg/sudipto%23%3Eselect * where { ?case nyon:hasAuthor :YChandrachud . ?case ?p ?o . }&format=json')
    .then(res => res.json())
.then(async json => {
      let ans = JSON.stringify(json.results.bindings);
      ans = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: `use the following json from sparql query response to construct a natural langiage answer: ${ans}`,
        temperature: 0,
        max_tokens: 200,
      });
      res.status(200).json({ answer: ans.data.choices[0].text || 'Sorry, I could not understand that.' });
    })
      .catch(err => console.error('error:' + err));
    
   return;
  }
 
  const response = await openai.createCompletion({
    model: "text-davinci-003",
    prompt: `use the following context
    prefix schema: <http://schema.org/>
prefix dc: <http://purl.org/dc/elements/1.1/>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix nyon: <https://w3id.org/def/NyOnLegalOntology#>
prefix : <https://cs.du.ac.in/kg/sudipto#>

    to generate sparql query without prefixes from text prompt, consider entities having prefix as :
    
    ${query}`,
    temperature: 0,
    max_tokens: 200,
  });
  
  console.log(response.data.choices[0].text);
  
  // run sparql query on blazegraph
  const q = `http://localhost:9999/blazegraph/sparql?query=prefix nyon: <https://w3id.org/def/NyOnLegalOntology%23>
prefix : <https://cs.du.ac.in/kg/sudipto%23>
%20
` + response.data.choices[0].text + '&format=json';
  fetch(q.replace(/\n/g, '%20').replace(/#/g, '%23'))
    .then(res => res.json())
    .then(async json => {
      let ans = JSON.stringify(json.results.bindings);
      ans = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: `use the following json from sparql query response to construct a natural langiage answer: ${ans}`,
        temperature: 0,
        max_tokens: 200,
      });
      res.status(200).json({ answer: response.data.choices[0].text || 'Sorry, I could not understand that.' });
    })
    .catch(err => console.error('error:' + err));
    
    
  // return res.status(200).json({ answer: 'Sorry, I could not understand that.' });
}
