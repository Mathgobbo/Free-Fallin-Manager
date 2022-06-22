

class Plane:
  def __init__(self, name: int, model: str, capacity_limit:str ) -> None:
    self.__capacity_limit = capacity_limit
    self.__model = model
    self.__name = name

  
  @property
  def capacity_limit(self):
    return self.__capacity_limit

  @capacity_limit.setter
  def capacity_limit(self, value: int):
    self.__capacity_limit = value
  
  @property
  def model(self):
    return self.__model

  @model.setter
  def model(self, value: str):
    self.__model = value

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value: str):
    self.__name = value