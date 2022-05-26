

from FlyingMemberTypeEnum import FlyingMemberTypeEnum


class FlyingMember:
  def __init__(self, cpf: str, name:str, phone:str, type: FlyingMemberTypeEnum, weight: float,height: float  ):
    self.__cpf = cpf
    self.__name = name
    self.__phone= phone
    self.__type = type
    self.__weight = weight
    self.__height = height

  @property
  def cpf(self): 
    return self.__cpf
  
  @cpf.setter
  def cpf(self, value:str):
    self.__cpf = value

  @property
  def name(self): 
    return self.__name
  
  @name.setter
  def name(self, value:str):
    self.__name = value

  @property
  def phone(self): 
    return self.__phone
  
  @phone.setter
  def phone(self, value:str):
    self.__phone = value

  @property
  def type(self): 
    return self.__type
  
  @type.setter
  def type(self, value:FlyingMemberTypeEnum):
    self.__type = value

  @property
  def weight(self): 
    return self.__weight
  
  @weight.setter
  def weight(self, value:float):
    self.__weight = value

  @property
  def height(self): 
    return self.__height
  
  @height.setter
  def height(self, value:float):
    self.__height = value

