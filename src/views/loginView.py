from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QApplication
from PyQt5 import uic
from src.models.Admin import Admin

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
    
    # Abre a tela
    def openView(self):
        self.show()

    # Chama o controllador e passa os valores dos campos de texto
    def login(self):
        print(self.usernameInput.text())
        print(self.passwordInput.text())
        self.__controller.Login(self.usernameInput.text(),self.passwordInput.text())
    
    # Atualiza mensagem de erro
    def emptyFields(self):
        self.messageError.setText("Preencha os campos obrigatórios!")

    # Atualiza mensagem de erro
    def invalidUser(self):
        self.messageError.setText("Usuário ou senha estão incorretos!")