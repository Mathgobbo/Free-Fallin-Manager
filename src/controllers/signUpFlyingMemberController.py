from src.models.FlyingMember import FlyingMember
from src.views.signUpFlyingMemberView import SignUpFlyingMemberView
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel

class SignUpFlyingMemberController:
    def __init__(self) -> None:
        self.__view = SignUpFlyingMemberView()

        self.cpfInput = self.findChild(QLineEdit, "cpfInput")
        self.cpfError = self.findChild(QLabel, "cpfError")

        self.nameInput = self.findChild(QLineEdit, "nameInput")
        self.nameError = self.findChild(QLabel, "nameError")

        self.phoneInput = self.findChild(QLineEdit, "phoneInput")
        self.phoneError = self.findChild(QLabel, "phoneError")

        self.weightInput = self.findChild(QLineEdit, "weightInput")
        self.weightError = self.findChild(QLabel, "weightError")

        self.heightInput = self.findChild(QLineEdit, "heightInput")
        self.heightError = self.findChild(QLabel, "heightError")

        

    def openView(self):
        self.__view.show()
    
    def isEmpty(self, flyingMember):
        if flyingMember.cpf() != "" and flyingMember.name() != "" and flyingMember.phone() != "" and flyingMember.weight() != "" and flyingMember.height() != "":
            return True
        return False
    
    def signUp(self):
        isValid = self.isFormValid()
        if (not isValid):
            return
        
        # Ta faltando o tipo
        newFlyingMember = FlyingMember(self.cpfInput.text(), self.nameInput.text(), self.phoneInput.text(), self.weightInput.text(), self.heightInput.text())
    
    def isFormValid(self):
        isValid = True

        self.cpfError.setText("")
        self.nameError.setText("")
        self.phoneError.setText("")
        self.weight.setText("")
        self.height.setText("")

        if(self.cpfInput.text() == ""):
            self.cpfError.setText("Insira seu CPF")
            isValid =  False
        
        if(self.nameInput.text() == ""):
            self.nameError.setText("Insira seu Nome")
            isValid =  False
        
        if(self.phoneInput.text() == ""):
            self.phoneError.setText("Insira seu número de telefone")
            isValid =  False
        
        if(self.weightInput.text() == ""):
            self.weightError.setText("Insira seu peso")
            isValid =  False
        
        if(self.heightInput.text() == ""):
            self.heightError.setText("Insira sua altura")
            isValid =  False
        
        return isValid
