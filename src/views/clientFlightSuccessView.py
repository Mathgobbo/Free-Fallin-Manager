

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QRadioButton, QDoubleSpinBox, QScrollArea, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QToolButton
from PyQt5.QtGui import QShowEvent

from src.models.FlyingMemberTypeEnum import FlyingMemberTypeEnum



class ClientFlightSuccessView(QMainWindow):

    def __init__(self, controller):
        super(ClientFlightSuccessView, self).__init__()
        self.__controller = controller
        uic.loadUi(r'.\src\resources\clientFlightSuccess.ui', self)
        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)

    
    def backButtonClick(self):
        self.close()
        self.__controller.back()


