from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QComboBox, QPushButton, QSpinBox


class FlightsListView(QMainWindow):

    def __init__(self, controller) -> None:
        super(FlightsListView, self).__init__()
        uic.loadUi(r'.\src\resources\listingFlights.ui', self)

        self.__controller = controller
    
    def openFlightsListView(self):
        self.show()