import Head from 'next/head'
import Image from 'next/image'
import { Inter } from '@next/font/google'
import styles from '@/styles/Chat.module.css'
import { DetailedHTMLProps, FormEventHandler, useState } from 'react'
import Messages from './_messages'

const inter = Inter({ subsets: ['latin'] })

export default function Chat() {
  const [q, setQ] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSubmit: FormEventHandler = (event: any) => {
    event.preventDefault()
    const data = new FormData(event.target)
    const query = data.get('query') || null;
    console.log(query);

    setMessages(messages => [...messages, { author: 'Q', content: query }]);
    setQ('');

    fetch('/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ query })
    })
      .then(res => res.json())
      .then(data => {
        console.log(data);
        setMessages(messages => [...messages, { author: 'A', content: data.answer.toLowerCase() || 'No answer found.' }]);
      })
  }

  const sendQuery = (query: string) => {
    setMessages(messages => [...messages, { author: 'Q', content: query }]);
    setQ('');

    fetch('/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ query })
    })
      .then(res => res.json())
      .then(data => {
        console.log(data);
        setMessages(messages => [...messages, { author: 'A', content: data.answer.toLowerCase() || 'No answer found.' }]);
      })
  }

  const handleQueryChange: any = (event: any) => {
    setQ(event.target.value);
  }

  return (
    <>
      <Head>
        <title>KanoonQA</title>
        <meta name="description" content="Legal QA" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        <div className={styles.description + ' ' + styles.typewriter}>
          <span>
            KanoonQA
          </span>
        </div>

        <div className={styles.kanoonform}>
          <Messages messages={messages} setMessages={setMessages} />

          <div className={styles.options}>
            <button className="option" onClick={() => sendQuery('get all data in kg')} >get all data in kg</button>
            <button className="option" onClick={() => sendQuery('get a case from 1977')}>get a case from 1977</button>
            <button className="option" onClick={() => sendQuery('get case name whose judgement whose author\'s name is justice y chandrachud')}>get case name whose judgement authored by justice y chandrachud</button>
          </div>

          <form action="/chat" onSubmit={handleSubmit}>
            <input type="text" name="query" placeholder="What is the meaning of life?" value={q} onChange={handleQueryChange}></input>
            <input type="submit" value="Send"></input>
          </form>
        </div>
      </main>
    </>
  )
}
