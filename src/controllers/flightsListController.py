from src.models.Fly import Fly
from src.views.flightsListView import FlightsListView
from src.dao.flightDao import FlightDao


class FlightsListController:
    def __init__(self, app, flightDao) -> None:
        self.__app = app
        self.__flightDao = flightDao
        self.__view = FlightsListView(self)
    
    def openView(self):
        self.__view.show()
    
    def goToAddFlight(self):
        self.__app.openFlightRegistrationView()
    
    def back(self):
        self.__app.openAdminMenu()
    
    def getFlights(self):
        return self.__flightDao.getAll()
