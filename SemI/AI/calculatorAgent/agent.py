from random import random
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.misc.utility import display_message, start_loop
from pade.behaviours.protocols import Behaviour

def sum(a, b):
    return a + b

class SumBehaviour(Behaviour):
    def __init__(self, agent, a, b):
        super().__init__(agent)
        self.a = a
        self.b = b

    def on_start(self):
        super().on_start()
        display_message(
          self.agent.aid.localname, 
          'Agent<{}> Sum({}, {}): {}'.format(
            self.agent.aid.name,
            self.a, self.b,
            sum(self.a, self.b)
          )
        )

class SumAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid=aid, debug=False)
        a = int(random() * 10)
        b = int(random() * 10)
        self.behaviours.append(SumBehaviour(self, a, b))

if __name__ == '__main__':
    agents = []
    agents_per_process = 5
    port, shift = int(2e4), 10

    for i in range(agents_per_process):
        agent_name = 'sum_agent_{}@localhost:{}'.format(i, port)
        agent = SumAgent(AID(name=agent_name))
        agents.append(agent)
        port += shift

    start_loop(agents)
