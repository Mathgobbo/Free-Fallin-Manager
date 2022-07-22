

from src.models.FlyingMemberTypeEnum import FlyingMemberTypeEnum
from src.models.FlyingRequest import FlyingRequest
from src.views.flightRequestApprovalFormView import \
    FlightRequestApprovalFormView


class FlightRequestApprovalFormController: 
  
    def __init__(self, app, flightRequestDao, membersDao) -> None:
        self.__app = app
        self.__flightRequestDao = flightRequestDao
        self.__membersDao = membersDao
        self.__view = FlightRequestApprovalFormView(self)
        self.__selectedFlyingRequest = None

    def openView(self, selectedFlyingRequest):
        self.__selectedFlyingRequest= selectedFlyingRequest
        self.__view.show()

    def getSelectedFlightRequest(self):
        return self.__selectedFlyingRequest

    def getInstructors(self):
        members = self.__membersDao.getAll()
        instructors = []
        for member in members:
            if(member.type == FlyingMemberTypeEnum.INSTRUTOR):
                instructors.append(member)
        return instructors

    def back(self):
        self.__app.openMainMenu()

    
