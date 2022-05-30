from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel

from src.models.Admin import Admin


class AdminListView(QMainWindow):
    
    def __init__(self, controller):
        super(AdminListView, self).__init__()
        self.__controller = controller
        uic.loadUi(r'.\src\resources\adminList.ui', self)
      

        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)
        self.addAdminButton = self.findChild(QPushButton, "addAdminButton")
        self.addAdminButton.clicked.connect(self.openSignUpAdmin)

    def openSignUpAdminView(self):
        self.__controller
    
    def backButtonClick(self):
        self.close()
        self.__controller.back()

    def openSignUpAdmin(self):
        self.__controller.goToSignUpAdmin()

