from Enviroment import Enviroment
from Agent import Agent

if __name__ == '__main__':
  entrada = input('Digite a configuração do ambiente: isDirtyA, isDirtyB, agentLocation ').split()
  entrada = [True if x=='True' else False for x in entrada ]
  env = Enviroment(entrada[0],entrada[1],entrada[2])
  steps = int(input('Digite o número de ações: '))
  
  agent = Agent()
  
  for i in range(steps):
    p = agent.perceives(env)
    sala = 'A' if p.getLocation() else 'B'
    estado = 'suja' if p.getIsDirty() else 'limpa'

    print('Agente está na sala ' + sala+ ' que está '+estado)
    act = agent.act(p)
    env.update(act)
    print('Ação realizada: ' + act)
    
    p = agent.perceives(env)
    sala = 'A' if p.getLocation() else 'B'
    estado = 'suja' if p.getIsDirty() else 'limpa'

    print('Situação após a ação: Sala '+sala+' estado '+estado)


   