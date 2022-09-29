class Perception:
  
  def __init__(self, location = True, isDirty = True):
    self.__location = location
    self.__isDirty = isDirty
    
  def getLocation(self):
    return self.__location
      
  def setLocation(self, location):
    self.__location = location
    
  def getIsDirty(self):
    return self.__isDirty
  
  def setIsDirty(self, isDirty):
    self.__isDirty = isDirty