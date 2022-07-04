from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QComboBox, QPushButton, QSpinBox


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

        self.weightInput = self.findChild(QSpinBox, "weightInput")
        self.weightError = self.findChild(QLabel, "weightError")

        self.heightInput = self.findChild(QSpinBox, "heightInput")
        self.heightError = self.findChild(QLabel, "heightError")

        self.typeInput = self.findChild(QComboBox, "comboBox")

        self.signUpButton = self.findChild(QPushButton, "cadastrar")
        self.signUpButton.clicked.connect(self.signUp)

        self.voltarBotao = self.findChild(QPushButton, "voltarBotao")
        self.voltarBotao.clicked.connect(self.voltarBotaoClick)


    def openSignUpFlyingMemberView(self):
        self.show()

    def signUp(self):
        self.__controller.signUp()
    
    def voltarBotaoClick(self):
        self.close()
        self.__controller.back()

    def clearInputs(self):
        self.nameInput.setText("")
        self.cpfInput.setText("")
        self.phoneInput.setText("")