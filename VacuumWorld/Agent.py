from Perception import Perception

class Agent:
  def __init__(self):
    pass
  
  def perceives(self, env):
    
    p = Perception()
    p.setLocation(env.getAgentLocation()) 
    
    if env.getAgentLocation():
      p.setIsDirty(env.getIsDirtyA())
    else:
      p.setIsDirty(env.getIsDirtyB())
    
    return p
  
  def act(self, perc):
    
    if perc.getIsDirty():
      return 'aspirar'
    elif perc.getLocation():
      return 'direita'
    else:
      return 'esquerda'