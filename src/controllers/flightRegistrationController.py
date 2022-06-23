from src.models.Fly import Fly
from src.views.flightRegistrationView import FlightRegistrationView


class FlightRegistrationController:

    def __init__(self, app, planeDao, flyMemberDao) -> None:
        self.__planeDao = planeDao
        self.__flyMemberDao = flyMemberDao
        self.__app = app
        self.__view = FlightRegistrationView(self)

    def openView(self):
        self.__view.show()

    def goToAddMember(self):
        self.__app.openAddMemberView()
    
    def getPlanes(self):
        return self.__planeDao.getAll()
    
    def getFlyMembers(self):
        return self.__flyMemberDao.getAll()
