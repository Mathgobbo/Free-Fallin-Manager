from src.models.Fly import Fly
from src.views.flightRegistrationView import FlightRegistrationView


class FlightRegistrationController:

    def __init__(self, app, planeDao, flyMemberDao, flightDao) -> None:
        self.__planeDao = planeDao
        self.__flyMemberDao = flyMemberDao
        self.__app = app
        self.__view = FlightRegistrationView(self)
        self.__flyMembers = []
        self.__flightDao = flightDao

    def openView(self):
        self.__view.show()

    def goToAddMember(self):
        self.__app.openAddMemberView()
    
    def getPlanes(self):
        return self.__planeDao.getAll()
    
    def getFlyMembers(self):
        return self.__flyMemberDao.getAll()

    def addFlyMembers(self, flyMember):
        for i in self.__flyMemberDao.getAll():
            memberStr = i.name + " - " + i.type
            if memberStr == flyMember:
                self.__flyMembers.append(i)

    def getFlyMembersList(self):
        return self.__flyMembers

    def flightRegistrationSubmit(self):
        selectedPlane = None
        for plane in self.getPlanes():
            if self.__view.planeComboBox.currentText() == plane.name: 
                selectedPlane = plane

        newFlight = Fly(self.__view.dateTimeEditInput.dateTime(), self.__flyMembers, selectedPlane)
        self.__flightDao.add(str(self.__view.dateTimeEditInput.dateTime()), newFlight)
        self.back()
    
    def goToFlightsList(self):
        self.__app.openFlightsListView()
    
    def back(self):
        self.__view.close()
        self.__app.openFlightsListView()

    def isFlightValid(self):
        pass
