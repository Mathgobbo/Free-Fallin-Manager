

from src.models.Fly import Fly
from src.models.FlyingMember import FlyingMember


class FlyingRequest:
  def __init__(self, done: bool, fly: Fly, user: FlyingMember):
    self.__done = done
    self.__fly = fly 
    self.__user = user
   
  @property
  def user(self):
    return self.__user

  @user.setter
  def user(self, value: FlyingMember):
    self.__user = value

   
  @property
  def fly(self):
    return self.__fly

  @fly.setter
  def fly(self, value: Fly):
    self.__fly = value

   
  @property
  def done(self):
    return self.__done

  @done.setter
  def done(self, value: bool):
    self.__done = value