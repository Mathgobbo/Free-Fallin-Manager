

from src.models.FlyingRequest import FlyingRequest
from src.views.flightRequestApprovalListView import FlightRequestApprovalListView


class FlightRequestApprovalListController: 
  
    def __init__(self, app, flightRequestDao) -> None:
        self.__app = app
        self.__flightRequestDao = flightRequestDao
        self.__view = FlightRequestApprovalListView(self)

    def openView(self):
        self.__view.show()

    def back(self):
        self.__app.openMainMenu()

    def getFlightRequests(self):
        return self.__flightRequestDao.getAll();
    
    def nextStep(self, flightRequest):
        self.__app.openFlightsRequestsApprovalForm(flightRequest)