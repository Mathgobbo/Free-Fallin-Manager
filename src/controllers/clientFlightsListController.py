

from src.views.clientFlightsListView import ClientFlightsListView


class ClientFlightsListController: 
  
    def __init__(self, app, flightsDao) -> None:
        self.__app = app
        self.__flightsDao = flightsDao
        self.__view = ClientFlightsListView(self)

    def openView(self):
        self.__view.show()

    def goToAddMember(self):
        self.__app.openAddMemberView()

    def getFlights(self):
        return self.__flightsDao.getAll();