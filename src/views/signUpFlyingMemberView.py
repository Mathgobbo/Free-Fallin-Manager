from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow


class SignUpFlyingMemberView(QMainWindow):

    def __init__(self, controller) -> None:
        super(SignUpFlyingMemberView, self).__init__()
        uic.loadUi(r'.\src\resources\signUpFlyingMember.ui', self)

        self.__controller = controller
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


    def openSignUpFlyingMemberView(self):
        self.show()
