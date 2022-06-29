from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QComboBox, QPushButton, QSpinBox, QTableWidget, QDateTimeEdit
from src.models.Fly import Fly
from src.models.FlyingMemberTypeEnum import FlyingMemberTypeEnum


class EditFlightView(QMainWindow):

    def __init__(self, controller):
        self.__controller = controller
        super(EditFlightView, self).__init__()
        uic.loadUi(r'.\src\resources\editFlight.ui', self)

        self.dataHoraInput = self.findChild(QDateTimeEdit, "dataHora")

        self.salvarBotao = self.findChild(QPushButton, "salvarBotao")
        self.salvarBotao.clicked.connect(self.salvarVooClick)

        self.voltarBotao = self.findChild(QPushButton, "voltarBotao")
        self.voltarBotao.clicked.connect(self.voltarBotaoClick)

        self.memberAddBotao = self.findChild(QPushButton, "memberAdd")
        self.memberAddBotao.clicked.connect(self.addMemberVooClick)

        self.tablePiloto = self.findChild(QTableWidget, "tablePiloto")
        self.tableInstrutores = self.findChild(QTableWidget, "tableInstrutores")
        self.tableAlunos = self.findChild(QTableWidget, "tableAlunos")
        self.tablePassageiros = self.findChild(QTableWidget, "tablePassageiros")


    def showEvent(self, ev):
        self.planeComboBox.clear()

        for i in self.__controller.getPlanes():
            self.planeComboBox.addItem(i.name)
        
        self.membersComboBox.clear()
        for j in self.__controller.getMembers():
            self.membersComboBox.addItem(j.name + " - " + j.type)
        
        return super(EditFlightView, self).showEvent(ev)
    
    def addMemberVooClick(self):
        flyMember = self.membersComboBox.currentText()
        self.__controller.addFlyMembers(flyMember)
        self.loadData()
    
    def loadData(self):
        membersList = self.__controller.getFlyMembersList()

        self.tablePiloto.setRowCount(3)
        self.tableInstrutores.setRowCount(3)
        self.tableAlunos.setRowCount(3)
        self.tablePassageiros.setRowCount(3)
        row = 0

        for i in membersList:
            if FlyingMemberTypeEnum(i.type) == FlyingMemberTypeEnum.PILOTO:
                memberName = QLabel(i.name)
                self.tablePiloto.setCellWidget(row, 0, memberName)
            
            if FlyingMemberTypeEnum(i.type) == FlyingMemberTypeEnum.INSTRUTOR:
                memberName = QLabel(i.name)
                self.tableInstrutores.setCellWidget(row, 0, memberName)
            
            if FlyingMemberTypeEnum(i.type) == FlyingMemberTypeEnum.ALUNO:
                memberName = QLabel(i.name)
                self.tableAlunos.setCellWidget(row, 0, memberName)
            
            if FlyingMemberTypeEnum(i.type) == FlyingMemberTypeEnum.PASSAGEIRO:
                memberName = QLabel(i.name)
                self.tablePassageiros.setCellWidget(row, 0, memberName)

    def openEditFlightView(self, flight):
        self.show()
    
    def goToAddMembro(self):
        self.close()

    
    def salvarVooClick(self):
        self.__controller.atualizarVoo()

    def voltarBotaoClick(self):
        self.close()
        self.__controller.goToFlightList()
