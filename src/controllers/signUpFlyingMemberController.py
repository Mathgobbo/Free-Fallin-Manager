from src.models.FlyingMember import FlyingMember
from src.views.signUpFlyingMemberView import SignUpFlyingMemberView
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel

class SignUpFlyingMemberController:
    def __init__(self, app) -> None:
        self.__app = app
        self.__view = SignUpFlyingMemberView(self)

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

        self.view.cpfError.setText("")
        self.view.nameError.setText("")
        self.view.phoneError.setText("")
        self.view.weight.setText("")
        self.view.height.setText("")

        if(self.view.cpfInput.text() == ""):
            self.view.cpfError.setText("Insira seu CPF")
            isValid =  False
        
        if(self.view.nameInput.text() == ""):
            self.view.nameError.setText("Insira seu Nome")
            isValid =  False
        
        if(self.view.phoneInput.text() == ""):
            self.view.phoneError.setText("Insira seu número de telefone")
            isValid =  False
        
        if(self.view.weightInput.text() == ""):
            self.view.weightError.setText("Insira seu peso")
            isValid =  False
        
        if(self.view.heightInput.text() == ""):
            self.view.heightError.setText("Insira sua altura")
            isValid =  False
        
        return isValid
