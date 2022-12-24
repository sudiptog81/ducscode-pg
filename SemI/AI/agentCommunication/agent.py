from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.misc.utility import display_message, start_loop
from pade.acl.messages import ACLMessage

class SenderAgent(Agent):
    def __init__(self, aid, receiver_agent):
        super().__init__(aid=aid)
        self.receiver_agent = receiver_agent

    def on_start(self):
        super().on_start()
        display_message(
            self.aid.localname,
            'Sending message from Agent<{}>...'.format(self.aid.name)
        )
        self.call_later(3., self.send_message)

    def react(self, message):
        super().react(message)
        display_message(
            self.aid.localname,
            'Received message from Agent<{}> => {}'.format(
                message.sender.name,
                message.content
            )
        )

    def send_message(self):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(self.receiver_agent)
        message.set_content('Ping!')
        self.add_all_agents(message.receivers)
        self.send(message)

    def add_all_agents(self, receivers):
        for r in receivers:
            self.agentInstance.table[r.localname] = r

class ReceiverAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid=aid)

    def react(self, message):
        super().react(message)
        if message.content != 'IDENT':
            display_message(
                self.aid.localname,
                'Received message from Agent<{}> => {}'.format(
                    message.sender.name,
                    message.content
                )
            )
            self.send_message(AID(message.sender.name))
    
    def send_message(self, receiver):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(receiver)
        message.set_content('Pong!')
        self.add_all_agents(message.receivers)
        self.send(message)
    
    def add_all_agents(self, receivers):
        for r in receivers:
            self.agentInstance.table[r.localname] = r

if __name__ == '__main__':
    agents = []
    receiver_agent = ReceiverAgent(AID(name='receiver@localhost:8000'))
    agents.append(receiver_agent)
    sender_agent = SenderAgent(AID(name='sender@localhost:8001'), receiver_agent.aid)
    agents.append(sender_agent)
    start_loop(agents)
