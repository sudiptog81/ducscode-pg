from random import random
from pade.core.agent import Agent
from pade.misc.utility import display_message, start_loop
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour

class CustomTimedBehaviour(TimedBehaviour):
  def __init__(self, agent, time):
    super().__init__(agent, time)
    

  def on_time(self):
    super().on_time()
    display_message(self.agent.aid.localname, 'Hello World from Agent<{}>!'.format(self.agent.aid.name))

class TimedAgent(Agent):
  def __init__(self, aid):
    super().__init__(aid)
    random_time = random() * 10 % 20 + 1
    self.behaviours.append(CustomTimedBehaviour(self, random_time))

if __name__ == '__main__':
  agents = []
  port, shift = int(2e4), 10
  agents_per_process = 5
  for i in range(agents_per_process):
    agents.append(TimedAgent(AID(name='timed_agent_{}@localhost:{}'.format(i, port))))
    port += shift
  start_loop(agents)

