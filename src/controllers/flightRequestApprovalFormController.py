

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
        self.__selectedInstructors = []

    def openView(self, selectedFlyingRequest):
        self.__selectedFlyingRequest= selectedFlyingRequest
        self.__view.show()

    def getSelectedFlightRequest(self):
        return self.__selectedFlyingRequest

    def getSelectedInstructors(self):
        return self.__selectedInstructors

    def getInstructors(self):
        members = self.__membersDao.getAll()
        instructors = []
        for member in members:
            if(str(member.type) == str(FlyingMemberTypeEnum.INSTRUTOR.value) and (not self.isInstructorSelected(member))):
                instructors.append(member)
        return instructors
    
    def isInstructorSelected(self, member):
        for selectedInstructor in self.__selectedInstructors:
            if(member.cpf == selectedInstructor.cpf):
                return True
        return False
    
    def addInstructor(self, instructor):
        members = self.__membersDao.getAll()
        for member in members:
            if(member.name + " - " + member.type == instructor):
                self.__selectedInstructors.append(member)
    
    def removeInstructor(self, instructor):
        newInstructors = []
        for selectedInstructor in self.__selectedInstructors:
            if instructor.cpf != selectedInstructor.cpf:
                newInstructors.append(selectedInstructor)
        self.__selectedInstructors = newInstructors
    
    def back(self):
        self.__view.close()
        self.__app.openFlightsRequestsApprovalList()

    def submitReject(self):
        key = str(self.__selectedFlyingRequest.fly.date_time)+"-"+self.__selectedFlyingRequest.fly.plane.name+"-"+self.__selectedFlyingRequest.user.cpf
        print(key)
        self.__flightRequestDao.remove(key)
        self.back()

    
