class Enviroment:
  
  def __init__(self, isDirtyA, isDirtyB, agentLocation):
    self.__isDirtyA = isDirtyA
    self.__isDirtyB = isDirtyB
    self.__agentLocation = agentLocation
    
  def getIsDirtyA(self):
    return self.__isDirtyA
  
  def setIsDirtyA(self, isDirtyA):
    self.__isDirtyA = isDirtyA
  
  def getIsDirtyB(self):
    return self.__isDirtyB
  
  def setIsDirtyB(self, isDirtyB):
    self.__isDirtyB = isDirtyB
  
  def getAgentLocation(self):
    return self.__agentLocation
  
  def setAgentLocation(self, agentLocation):
    self.__agentLocation = agentLocation
    
  def update(self, action):
    
    if action=='aspirar':
      if self.__agentLocation and self.__isDirtyA: #limpa A
        self.__isDirtyA=False
      elif self.__agentLocation==False and self.__isDirtyB:
        self.__isDirtyB=False
        
    elif action=='direita':
      if self.__agentLocation:      #se estiver na sala A
        self.setAgentLocation(False)   #vai pra sala B
        
    elif action=='esquerda':
      if not self.__agentLocation: #se não estiver na sala A
        self.setAgentLocation(True)   #vai pra sala A
      
        
        