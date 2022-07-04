from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QSpinBox, QComboBox
from src.models.FlyingMember import FlyingMember


class EditMemberView(QMainWindow):
    def __init__(self, controller):
        self.__controller = controller
        super(EditMemberView, self).__init__()
        uic.loadUi(r'.\src\resources\editFlyingMember.ui', self)

        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)

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

        self.saveButton = self.findChild(QPushButton, "saveButton")
        self.saveButton.clicked.connect(self.save)
    
    def save(self):
        self.__controller.save()
    
    def openEditMemberView(self, member):
        self.show()
        self.nameInput.setText(member.name)
        self.cpfInput.setText(member.cpf)
        self.phoneInput.setText(member.phone)
        self.typeInput.setCurrentText(member.type)
        # self.weightInput.setValue(member.weight)
        # self.heightInput.setValue(member.height)

    def backButtonClick(self):
        self.close()
        self.__controller.back()
    
    def clearInputs(self):
        self.nameInput.setText("")
        self.cpfInput.setText("")
        self.phoneInput.setText("")