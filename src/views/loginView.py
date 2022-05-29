from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QApplication
from PyQt5 import uic

class LoginView(QMainWindow):
    def __init__(self, controller):
        self.__controller = controller
        super(LoginView, self).__init__()
        uic.loadUi(r'C:\free-fallin-manager\src\resources\login.ui',self)

        self.usernameInput = self.findChild(QLineEdit, "username")
        self.passwordInput = self.findChild(QLineEdit, "password")
        self.enterButton = self.findChild(QPushButton, "enterButton")
        self.messageError = self.findChild(QLabel, "message")

        self.enterButton.clicked.connect(self.login)
    
    def openView(self):
        self.show()

    def login(self):
        print(self.usernameInput.text())
        print(self.passwordInput.text())
        self.__controller.Login(self.usernameInput.text(), self.passwordInput.text())
    
    def emptyFields(self):
        self.messageError.setText("Preencha os campos obrigatórios!")

    def invalidUser(self):
        self.messageError.setText("Usuário ou senha estão incorretos!")