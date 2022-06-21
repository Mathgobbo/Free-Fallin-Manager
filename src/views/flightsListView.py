from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QComboBox, QPushButton, QSpinBox


class FlightsListView(QMainWindow):

    def __init__(self, controller) -> None:
        super(FlightsListView, self).__init__()
        uic.loadUi(r'.\src\resources\listingFlights.ui', self)

        self.__controller = controller

        self.addFlightButton = self.findChild(QPushButton, "addFlightButton")
        self.addFlightButton.clicked.connect(self.goToAddFlight)
    
    def openFlightsListView(self):
        self.show()
    
    def goToAddFlight(self):
        self.__controller.goToAddFlight()