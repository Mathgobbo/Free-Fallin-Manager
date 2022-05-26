
from multiprocessing.dummy import Array
from sqlite3 import Timestamp

from src.models.FlyingMember import FlyingMember
from src.models.Plane import Plane


class Fly:
  def __init__(self, date_time: Timestamp, members: FlyingMember, plane: Plane ) -> None:
    self.__members = members
    self.__date_time = date_time
    self.__plane = plane 

  
  @property
  def members(self):
    return self.__members

  @members.setter
  def members(self, value: FlyingMember):
    self.__members = value

  
  @property
  def date_time(self):
    return self.__date_time

  @date_time.setter
  def date_time(self, value: Timestamp):
    self.__date_time = value

  
  @property
  def plane(self):
    return self.__plane

  @plane.setter
  def plane(self, value: Plane):
    self.__plane = value