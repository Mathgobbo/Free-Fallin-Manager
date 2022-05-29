from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel

from src.models.Admin import Admin


class SignUpAdminView(QMainWindow):
    
    def __init__(self, controller):
        self.__controller = controller
        super(SignUpAdminView, self).__init__()
        uic.loadUi(r'.\src\resources\signUpAdmin.ui', self)
        self.usernameInput = self.findChild(QLineEdit, "usernameInput")
        self.usernameError = self.findChild(QLabel, "usernameError")
     
        self.passInput = self.findChild(QLineEdit, "passInput")
        self.passError = self.findChild(QLabel, "passError")
      
        self.confirmPassInput = self.findChild(QLineEdit, "confirmPassInput")
        self.confirmPassError = self.findChild(QLabel, "confirmPassError")

        self.signUpButton = self.findChild(QPushButton, "pushButton")
        self.signUpButton.clicked.connect(self.signUp)

        self.backButton = self.findChild(QPushButton, "backButton")

    def openSignUpAdminView(self):
        self.show()
    
    def backButtonClick(self):
        self.close()

    def signUp(self):
        isValid = self.isFormValid()
        if(not isValid): 
            return
        
        newAdmin = Admin(self.usernameInput.text(), self.passInput.text())
        print(newAdmin)

    def isFormValid(self): 
        isValid = True

        self.usernameError.setText("")
        self.passError.setText("")
        self.confirmPassError.setText("")

        if(self.usernameInput.text() == ""):
            self.usernameError.setText("Insira um Nome de Usuário")
            isValid =  False
        if(self.passInput.text() == ""):
            self.passError.setText("Insira uma Senha")
            isValid =  False
        if(self.confirmPassInput.text() == ""):
            self.confirmPassError.setText("Confirme a senha informada")
            isValid =  False

        if(self.confirmPassInput.text() != self.passInput.text()):
            self.confirmPassError.setText("Confirmação de Senha está diferente da senha informada")
            isValid =  False


        return isValid
    

