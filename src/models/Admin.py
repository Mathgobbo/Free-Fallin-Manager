

class Admin:
  def __init__(self, username, password):
    self.__username = username
    self.__password = password


  @property
  def username(self): 
    return self.__username
  
  @username.setter
  def username(self, value:str):
    self.__username = value


  @property
  def password(self): 
    return self.__password
  
  @password.setter
  def password(self, value:str):
    self.__password = value
