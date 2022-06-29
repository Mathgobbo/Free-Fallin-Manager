from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QComboBox, QPushButton, QSpinBox
from src.models.Fly import Fly


class EditFlightView(QMainWindow):

    def __init__(self, controller):
        self.__controller = controller
        super(EditFlightView, self).__init__()
        uic.loadUi(r'.\src\resources\editFlight.ui', self)

        self.salvarBotao = self.findChild(QPushButton, "salvarBotao")
        self.salvarBotao.clicked.connect(self.salvarVooClick)

        self.voltarBotao = self.findChild(QPushButton, "voltarBotao")
        self.voltarBotao.clicked.connect(self.voltarBotaoClick)

    def openEditFlightView(self, flight):
        self.show()
    
    def salvarVooClick(self):
        self.__controller.atualizarVoo()

    def voltarBotaoClick(self):
        self.close()
        self.__controller.goToFlightList()
