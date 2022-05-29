from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class SignUpAdminView(QMainWindow):
    
    def __init__(self, controller):
        self.__controller = controller
        super(SignUpAdminView, self).__init__()
        uic.loadUi(r'.\src\resources\signUpAdmin.ui', self)

    def openSignUpAdminView(self):
        self.show()

