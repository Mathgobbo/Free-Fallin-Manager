from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QComboBox, QPushButton, QSpinBox, QDateTimeEdit, QTableWidget
from src.models.FlyingMemberTypeEnum import FlyingMemberTypeEnum


class FlightRegistrationView(QMainWindow):

    def __init__(self, controller) -> None:
        super(FlightRegistrationView, self).__init__()
        uic.loadUi(r'.\src\resources\flightRegistration.ui', self)
        self.__controller = controller

        self.tablePiloto = self.findChild(QTableWidget, "tablePiloto")
        self.tableInstrutores = self.findChild(QTableWidget, "tableInstrutores")
        self.tableAlunos = self.findChild(QTableWidget, "tableAlunos")
        self.tablePassageiros = self.findChild(QTableWidget, "tablePassageiros")

        self.addMembroButton = self.findChild(QPushButton, "addMembro")
        self.addMembroButton.clicked.connect(self.goToAddMembro)

        self.dateTimeEditInput = self.findChild(QDateTimeEdit, "dateTimeInput")

        self.planeComboBox = self.findChild(QComboBox, "planeComboBox")

        self.membersComboBox = self.findChild(QComboBox, "membersComboBox")

        self.addMembroVooButton = self.findChild(QPushButton, "addMembroVoo")
        self.addMembroVooButton.clicked.connect(self.addFlyMember)

        self.flightRegistrationButton = self.findChild(QPushButton, "flightRegistration")
        self.flightRegistrationButton.clicked.connect(self.flightRegistrationSubmit)

    def showEvent(self, ev):

        self.planeComboBox.clear()
        for i in self.__controller.getPlanes():
            self.planeComboBox.addItem(i.name)
        
        self.membersComboBox.clear()
        for j in self.__controller.getFlyMembers():
            self.membersComboBox.addItem(j.name + " - " + j.type)

        return super(FlightRegistrationView, self).showEvent(ev)
    
    def openFlightRegistrationView(self):
        self.show()
    
    def goToAddMembro(self):
        self.close()
        self.__controller.goToAddMember()

    def addFlyMember(self):
        flyMember = self.membersComboBox.currentText()
        self.__controller.addFlyMembers(flyMember)
        self.loadData()
    
    def loadData(self):
        membersList = self.__controller.getFlyMembersList()

        self.tablePiloto.setRowCount(1)
        row = 0

        for i in membersList:
            if FlyingMemberTypeEnum(i.type) == FlyingMemberTypeEnum.PILOTO:
                memberName = QLabel(i.name)
                print(memberName)
                self.tablePiloto.setCellWidget(row, 0, memberName)

    def flightRegistrationSubmit(self):
        self.__controller.flightRegistrationSubmit()