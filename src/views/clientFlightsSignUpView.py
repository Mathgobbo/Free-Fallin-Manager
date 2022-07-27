
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

        self.submitButton = self.findChild(QPushButton, "submitButton")
        self.submitButton.clicked.connect(self.submitForm)
        self.clientTypeError = self.findChild(QLabel, 'clientTypeError')



    def showEvent(self, ev: QShowEvent) -> None:
        flight = self.__controller.getSelectedFlight()
        self.flightDetails.setText(str(flight.date_time.toString()) + " - " + flight.plane.name + " - " + str(int(flight.plane.capacity_limit) - len(flight.members)))
        return super(ClientFlightsSignUpView, self).showEvent(ev)
    
    def backButtonClick(self):
        self.close()
        self.__controller.back()

    def cpfChanged(self):
        cpf = self.cpfInput.text()
        if len(cpf) != 14: 
            self.setEnabledForm(False)
            return
        members = self.__controller.getMembers()
        for member in members:
            if member.cpf == cpf:
                return self.fillInputs(member)
        self.setEnabledForm(True)
    
    def setEnabledForm(self, value):
        self.nameInput.setEnabled(value)
        self.phoneInput.setEnabled(value)
        self.weightInput.setEnabled(value)
        self.heightInput.setEnabled(value)
        self.passengerRadio.setEnabled(value)
        self.studentRadio.setEnabled(value)

    def fillInputs(self, member):
        self.nameInput.setText(member.name)
        self.phoneInput.setText(member.phone)
        self.weightInput.setValue(member.weight)
        self.heightInput.setValue(member.height)

        if FlyingMemberTypeEnum(member.type) == FlyingMemberTypeEnum.ALUNO:
            self.studentRadio.setChecked(True)
        if FlyingMemberTypeEnum(member.type) == (FlyingMemberTypeEnum.PASSAGEIRO):
            self.passengerRadio.setChecked(True)
    
    def isFormValid(self):
        isFormValid = True
        if len(self.cpfInput.text()) < 14:
            self.cpfError.setText("Insira seu CPF corretamente")
            isFormValid = False
        if self.nameInput.text() == "":
            self.nameError.setText("Insira seu nome")
            isFormValid = False
        if len(self.phoneInput.text()) < 13:
            self.phoneError.setText("Insira seu telefone corretamente")
            isFormValid = False
        if self.weightInput.value() == 0:
            self.weightError.setText("Insira seu peso em KG")
            isFormValid = False
        if self.heightInput.value() == 0:
            self.heightError.setText("Insira sua altura em CM")
            isFormValid = False
        if not self.studentRadio.isChecked() and not self.passengerRadio.isChecked():
            self.clientTypeError.setText("Selecione um dos dois.")
            isFormValid = False
        return isFormValid

    def cleanErrors(self):
        self.clientTypeError.setText("")
        self.nameError.setText("")
        self.cpfError.setText("")
        self.phoneError.setText("")
        self.weightError.setText("")
        self.heightError.setText("")

    def submitForm(self):
        self.cleanErrors()
        if not self.isFormValid():
            return
        
        memberType = None
        if self.studentRadio.isChecked():
            memberType = FlyingMemberTypeEnum.ALUNO.value
        elif self.passengerRadio.isChecked():
            memberType = FlyingMemberTypeEnum.PASSAGEIRO.value
        
        self.__controller.submit(
            self.nameInput.text(),
            self.cpfInput.text(),
            self.phoneInput.text(),
            self.heightInput.value(),
            self.weightInput.value(),
            memberType
        )
        self.clearForm()

    def clearForm(self):
        self.cpfInput.setText("")
        self.nameInput.setText("")
        self.phoneInput.setText("")
        self.heightInput.setValue(0)
        self.weightInput.setValue(0)
        self.studentRadio.setChecked(False)
        self.passengerRadio.setChecked(False)

        

        
