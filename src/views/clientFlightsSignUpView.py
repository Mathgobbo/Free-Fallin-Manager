from unicodedata import name
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QRadioButton, QDoubleSpinBox, QScrollArea, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QToolButton
from PyQt5.QtGui import QShowEvent

from src.models.FlyingMemberTypeEnum import FlyingMemberTypeEnum

class ClientFlightsSignUpView(QMainWindow):
    
    def __init__(self, controller):
        super(ClientFlightsSignUpView, self).__init__()
        self.__controller = controller
        uic.loadUi(r'.\src\resources\clientSignUpForm.ui', self)
        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)
        self.flightDetails = self.findChild(QLabel, "flightDetails")

        self.cpfInput = self.findChild(QLineEdit, 'cpfInput')
        self.cpfError = self.findChild(QLabel, 'cpfError')
        self.cpfInput.textChanged.connect(self.cpfChanged)

        self.nameInput = self.findChild(QLineEdit, 'nameInput')
        self.nameError = self.findChild(QLabel, 'nameError')

        self.phoneInput = self.findChild(QLineEdit, 'phoneInput')
        self.phoneError = self.findChild(QLabel, 'phoneError')

        self.weightInput = self.findChild(QDoubleSpinBox, 'weightInput')
        self.weightError = self.findChild(QLabel, 'weightError')

        self.heightInput = self.findChild(QDoubleSpinBox, 'heightInput')
        self.heightError = self.findChild(QLabel, 'heightError')

        self.passengerRadio = self.findChild(QRadioButton, "passengerRadio")
        self.studentRadio = self.findChild(QRadioButton, "studentRadio")


    def showEvent(self, ev: QShowEvent) -> None:
        flight = self.__controller.getSelectedFlight()
        self.flightDetails.setText(str(flight.date_time) + " - " + flight.plane.name + " - " + str(flight.plane.capacity_limit - len(flight.members)))
        return super(ClientFlightsSignUpView, self).showEvent(ev)
    
    def backButtonClick(self):
        self.close()
        self.__controller.back()

    def cpfChanged(self):
        cpf = self.cpfInput.text()
        if len(cpf) != 14: 
            return
        members = self.__controller.getMembers()
        for member in members:
            if member.cpf == cpf:
                return self.fillInputs(member)
        self.nameInput.setEnabled(True)
        self.phoneInput.setEnabled(True)
        self.weightInput.setEnabled(True)
        self.heightInput.setEnabled(True)

    def fillInputs(self, member):
        self.nameInput.setText(member.name)
        self.phoneInput.setText(member.phone)
        self.weightInput.setValue(member.weight)
        self.heightInput.setValue(member.height)

        if FlyingMemberTypeEnum(member.type) == FlyingMemberTypeEnum.ALUNO:
            self.studentRadio.setChecked(True)
        if FlyingMemberTypeEnum(member.type) == (FlyingMemberTypeEnum.PASSAGEIRO):
            self.passengerRadio.setChecked(True)


        

        
