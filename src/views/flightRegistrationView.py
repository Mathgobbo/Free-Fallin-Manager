from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QComboBox, QPushButton, QSpinBox, QDateTimeEdit, QTableWidget, QToolButton
from src.models.FlyingMemberTypeEnum import FlyingMemberTypeEnum
from PyQt5.QtGui import QIcon, QShowEvent


class FlightRegistrationView(QMainWindow):

    def __init__(self, controller) -> None:
        super(FlightRegistrationView, self).__init__()
        uic.loadUi(r'.\src\resources\flightRegistration.ui', self)
        self.__controller = controller

        self.botaoVoltar = self.findChild(QPushButton, "botaoVoltar")
        self.botaoVoltar.clicked.connect(self.botaoVoltarClick)

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

        self.flightError = self.findChild(QLabel, "validateLabel")

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

        rowPiloto = 0
        rowInstrutor = 0
        rowPassageiro = 0
        rowAluno = 0

        for i in membersList:
            if FlyingMemberTypeEnum(i.type) == FlyingMemberTypeEnum.PILOTO:
                self.tablePiloto.setRowCount(rowPiloto + 1)
                memberName = QLabel(i.name)
                self.tablePiloto.setCellWidget(rowPiloto, 0, memberName)
                deleteButton = QToolButton()
                deleteButton.setIcon(QIcon("./src/resources/trashIcon.png"))
                deleteButton.clicked.connect(self.deletePiloto)
                self.tablePiloto.setCellWidget(rowPiloto, 1, deleteButton)
                rowPiloto = rowPiloto + 1
          
            if FlyingMemberTypeEnum(i.type) == FlyingMemberTypeEnum.INSTRUTOR:
                self.tableInstrutores.setRowCount(rowInstrutor + 1)
                memberName = QLabel(i.name)
                self.tableInstrutores.setCellWidget(rowInstrutor, 0, memberName)
                deleteButton = QToolButton()
                deleteButton.setIcon(QIcon("./src/resources/trashIcon.png"))
                deleteButton.clicked.connect(self.deleteInstrutor)
                self.tableInstrutores.setCellWidget(rowInstrutor, 1, deleteButton)
                rowInstrutor = rowInstrutor + 1

            if FlyingMemberTypeEnum(i.type) == FlyingMemberTypeEnum.ALUNO:
                self.tableAlunos.setRowCount(rowAluno + 1)
                memberName = QLabel(i.name)
                self.tableAlunos.setCellWidget(rowAluno, 0, memberName)
                deleteButton = QToolButton()
                deleteButton.setIcon(QIcon("./src/resources/trashIcon.png"))
                deleteButton.clicked.connect(self.deleteAluno)
                self.tableAlunos.setCellWidget(rowAluno, 1, deleteButton)
                rowAluno = rowAluno + 1
            
            if FlyingMemberTypeEnum(i.type) == FlyingMemberTypeEnum.PASSAGEIRO:
                self.tablePassageiros.setRowCount(rowPassageiro + 1)
                memberName = QLabel(i.name)
                self.tablePassageiros.setCellWidget(rowPassageiro, 0, memberName)
                deleteButton = QToolButton()
                deleteButton.setIcon(QIcon("./src/resources/trashIcon.png"))
                deleteButton.clicked.connect(self.deletePassageiro)
                self.tablePassageiros.setCellWidget(rowPassageiro, 1, deleteButton)
                rowPassageiro = rowPassageiro + 1
        
    def flightRegistrationSubmit(self):
        self.__controller.flightRegistrationSubmit()

    def botaoVoltarClick(self):
        self.close()
        self.__controller.goToFlightsList()
    
    def deletePiloto(self):
        self.tablePiloto.setRowCount(0)
    
    def deletePassageiro(self):
        self.tablePassageiros.setRowCount(0)
    
    def deleteAluno(self):
        self.tableAlunos.setRowCount(0)
    
    def deleteInstrutor(self):
        self.tableInstrutores.setRowCount(0)
