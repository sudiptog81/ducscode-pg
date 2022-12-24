from pade.core.agent import Agent
from pade.misc.utility import display_message, start_loop
from pade.acl.aid import AID

class HelloAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid=aid)
        display_message(self.aid.localname, 'Hello World from Agent<{}>!'.format(self.aid.name))

if __name__ == '__main__':
    agents = []
    port, shift = int(2e4), 10
    agents_per_process = 5

    for i in range(agents_per_process):
        agents.append(HelloAgent(AID(name='hello_agent_{}@localhost:{}'.format(i, port))))
        port += shift
    
    start_loop(agents)
    