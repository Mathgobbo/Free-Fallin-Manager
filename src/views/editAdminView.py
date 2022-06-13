from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel
from models.Administrator import Admin


class EditAdminView(QMainWindow):
    
    def __init__(self, controller):
        self.__controller = controller
        super(EditAdminView, self).__init__()
        uic.loadUi(r'.\src\resources\editAdmin.ui', self)
        self.usernameInput = self.findChild(QLineEdit, "usernameInput")
        self.usernameError = self.findChild(QLabel, "usernameError")
     
        self.passInput = self.findChild(QLineEdit, "passInput")
        self.passError = self.findChild(QLabel, "passError")
      
        self.confirmPassInput = self.findChild(QLineEdit, "confirmPassInput")
        self.confirmPassError = self.findChild(QLabel, "confirmPassError")

        self.saveButton = self.findChild(QPushButton, "pushButton")
        self.saveButton.clicked.connect(self.save)

        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)

    def save(self):
        self.__controller.save()

    def openEditAdminView(self, admin):
        self.show()
        self.usernameInput.setText(admin.username)
        self.passInput.setText(admin.password)
        self.confirmPassInput.setText(admin.password)
    
    def backButtonClick(self):
        self.close()
        self.__controller.back()
    
    def clearInputs(self):
        self.usernameInput.setText("")
        self.passInput.setText("")
        self.confirmPassInput.setText("")
    
  

