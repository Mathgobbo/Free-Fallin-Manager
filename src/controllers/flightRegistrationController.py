from src.models.Fly import Fly
from src.views.flightRegistrationView import FlightRegistrationView
from datetime import datetime, timedelta


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
        isValid = self.isFlightValid()
        if (not isValid):
            return
        
        selectedPlane = None
        for plane in self.getPlanes():
            if self.__view.planeComboBox.currentText() == plane.name: 
                selectedPlane = plane
                total = plane.capacity_limit

        if len(self.__flyMembers) > total:
            return self.__view.flightError.setText("Erro ao cadastrar um voo, capacidade lotada.")

        newFlight = Fly(self.__view.dateTimeEditInput.dateTime(), self.__flyMembers, selectedPlane)
        self.__flightDao.add(str(self.__view.dateTimeEditInput.dateTime()), newFlight)
        self.__flyMembers = []
        print(str(self.__view.dateTimeEditInput.dateTime().toString(self.__view.dateTimeEditInput.displayFormat())))
        self.back()
    
    def goToFlightsList(self):
        self.__app.openFlightsListView()
    
    def back(self):
        self.__view.close()
        self.__app.openFlightsListView()

    def isFlightValid(self):
        self.__view.flightError.setText("")
        isValid = True

        flights = self.__flightDao.getAll()
        selectedFlightTime = self.__view.dateTimeEditInput.dateTime().toString(self.__view.dateTimeEditInput.displayFormat())
        selectedFlightTimeFormat = datetime.strptime(str(selectedFlightTime), "%m/%d/%Y %H:%S")

        m = 30
        selectedFlightTimeFormatAhead = selectedFlightTimeFormat + timedelta(minutes=m)
        selectedFlightTimeFormatBefore = selectedFlightTimeFormat - timedelta(minutes=m)

        for flight in flights:
            time = flight.date_time.toString(self.__view.dateTimeEditInput.displayFormat())
            flightTimeFormat = datetime.strptime(str(time), "%m/%d/%Y %H:%S")
        
            if flightTimeFormat > selectedFlightTimeFormatBefore and flightTimeFormat < selectedFlightTimeFormatAhead:
                self.__view.flightError.setText("Erro ao cadastrar um voo")
                isValid = False


        if self.__view.tablePiloto.rowCount() == 0 or self.__view.tablePiloto.rowCount() >= 2:
            self.__view.flightError.setText("Erro ao cadastrar um voo, piloto necessário.")
            isValid = False
    
        
        if self.__view.tableInstrutores.rowCount() == 0:
            self.__view.flightError.setText("Erro ao cadastrar um voo, instrutor necessário.")
            isValid = False
        
        if self.__view.tableAlunos.rowCount() > 0 and self.__view.tableInstrutores.rowCount() % self.__view.tableAlunos.rowCount() != 0:
            self.__view.flightError.setText("Erro ao cadastrar um voo.")
            isValid = False
        
        if self.__view.tablePassageiros.rowCount() > 0 and self.__view.tablePassageiros.rowCount() != self.__view.tableInstrutores.rowCount():
            self.__view.flightError.setText("Erro ao cadastrar um voo.")
            isValid = False
            
        
        return isValid
