from src.models.Fly import Fly
from src.views.editFlightView import EditFlightView
from src.dao.flightDao import FlightDao


class EditFlightController:
    def __init__(self, app, flightDao, planeDao, flyMemberDao) -> None:
        self.__planeDao = planeDao
        self.__flyMemberDao = flyMemberDao
        self.__view = EditFlightView(self)
        self.__app = app
        self.__flyMembers = []
        self.__flightDao = flightDao
        self.__selectedFlight = None
    
    def openView(self, flight):
        self.__selectedFlight = flight
        self.__view.openEditFlightView(flight)
    
    def getPlanes(self):
        return self.__planeDao.getAll()
    
    def getMembers(self):
        return self.__flyMemberDao.getAll()

    def goToFlightList(self):
        self.__app.openFlightsListView()
    
    def addFlyMembers(self, flyMember):
        for i in self.__flyMemberDao.getAll():
            memberStr = i.name + " - " + i.type
            if memberStr == flyMember:
                self.__flyMembers.append(i)
    
    def getFlyMembersList(self):
        return self.__flyMembers
