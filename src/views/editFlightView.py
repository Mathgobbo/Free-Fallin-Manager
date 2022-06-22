from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QComboBox, QPushButton, QSpinBox


class EditFlightView(QMainWindow):

    def __init__(self, controller):
        self.__controller = controller
        super(EditFlightView, self).__init__()
        uic.loadUi(r'.\src\resources\editFlight.ui', self)
    
    def openEditFlightView(self):
        self.show()
