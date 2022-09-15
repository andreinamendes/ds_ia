from Enviroment import Enviroment
from Agent import Agent

if __name__ == '__main__':
  
  env = Enviroment(True, True, True)
  steps = int(input('Digite o número de ações: '))
  
  agent = Agent()
  
  for i in range(steps):
    p = agent.perceives(env)
    print(p)
    act = agent.act(p)
    env.update(act)