

from src.views.clientFlightsListView import ClientFlightsListView


class ClientFlightsListController: 
  
    def __init__(self, app, flightsDao) -> None:
        self.__app = app
        self.__flightsDao = flightsDao
        self.__view = ClientFlightsListView(self)

    def openView(self):
        self.__view.show()

    def back(self):
        self.__app.openMainMenu()

    def getFlights(self):
        return self.__flightsDao.getAll();
    
    def nextStep(self, flight):
        self.__app.openClientSignUpToFlight(flight)