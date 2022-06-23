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
        self.backButton.clicked.connect(self.backButtonClick)

    def signUp(self):
        self.__controller.signUp()

    def openSignUpAdminView(self):
        self.show()
    
    def backButtonClick(self):
        self.close()
        self.__controller.back()
    
    def clearInputs(self):
        self.usernameInput.setText("")
        self.passInput.setText("")
        self.confirmPassInput.setText("")

  

