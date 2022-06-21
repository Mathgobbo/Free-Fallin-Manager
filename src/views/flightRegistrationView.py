from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QComboBox, QPushButton, QSpinBox


class FlightRegistrationView(QMainWindow):

    def __init__(self, controller) -> None:
        super(FlightRegistrationView, self).__init__()
        uic.loadUi(r'.\src\resources\flightRegistration.ui', self)

        self.__controller = controller
    
    def openFlightRegistrationView(self):
        self.show()