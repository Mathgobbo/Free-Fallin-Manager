

from src.models.FlyingMemberTypeEnum import FlyingMemberTypeEnum
from src.models.FlyingRequest import FlyingRequest
from src.models.FlyingMember import FlyingMember
from src.models.Fly import Fly
from src.views.clientFlightsSignUpView import ClientFlightsSignUpView


class ClientFlightsSignUpController: 
  
    def __init__(self, app, membersDao, flyingRequestDao) -> None:
        self.__app = app
        self.__membersDao = membersDao
        self.__flyingRequestDao = flyingRequestDao
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
    
    def submit(self, name: str, cpf: str, phone: str, height: float, weight: float, memberType: FlyingMemberTypeEnum):
        selectedMember = None
        for member in self.getMembers():
            if member.cpf == cpf:
                selectedMember = member
                break
        
        if selectedMember == None:
            selectedMember = FlyingMember(cpf, name, phone, memberType, weight, height)
            self.__membersDao.add(selectedMember.cpf, selectedMember)
        
        request = FlyingRequest(False, self.__selectedFlight, selectedMember)
        key = str(request.fly.date_time)+"-"+request.fly.plane.name+"-"+selectedMember.cpf
        self.__flyingRequestDao.add(key, request)

        self.__view.close()
        self.__app.openClientFlightSuccessPage()
        

        
        