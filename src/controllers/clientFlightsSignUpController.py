

from src.models.Fly import Fly
from src.views.clientFlightsSignUpView import ClientFlightsSignUpView


class ClientFlightsSignUpController: 
  
    def __init__(self, app, membersDao) -> None:
        self.__app = app
        self.__membersDao = membersDao
        self.__view = ClientFlightsSignUpView(self)
        self.__selectedFlight = None
         
    def openView(self, flight):
        self.__selectedFlight = flight
        self.__view.show()
    
    def getSelectedFlight(self) -> Fly:
      return self.__selectedFlight

    def back(self):
        self.__app.openFlightsToBook()

    def getMembers(self):
        return self.__membersDao.getAll()