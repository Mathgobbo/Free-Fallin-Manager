from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QComboBox, QPushButton, QSpinBox, QTableWidget, QTableWidgetItem, QToolButton
from PyQt5.QtGui import QIcon, QShowEvent


class FlightsListView(QMainWindow):

    def __init__(self, controller) -> None:
        super(FlightsListView, self).__init__()
        uic.loadUi(r'.\src\resources\listingFlights.ui', self)

        self.__controller = controller

        self.botaoVoltar = self.findChild(QPushButton, "botaoVoltar")
        self.botaoVoltar.clicked.connect(self.botaoVoltarClick)

        self.addFlightButton = self.findChild(QPushButton, "addFlightButton")
        self.addFlightButton.clicked.connect(self.goToAddFlight)

        self.flightsTable = self.findChild(QTableWidget, "flightsTable")
        self.flightsTable.setColumnWidth(0, 300)

    
    def openFlightsListView(self):
        self.show()
    
    def goToAddFlight(self):
        self.__controller.goToAddFlight()
    
    def botaoVoltarClick(self):
        self.close()
        self.__controller.back()
    
    def loadData(self):
        row = 0
        flights = self.__controller.getFlights()
        print(len(flights))
        self.flightsTable.setRowCount(len(flights))
        for flight in flights:
            planeName = QLabel(flight.plane.name)
            self.flightsTable.setCellWidget(row, 0, planeName)
            botao = QToolButton()
            botao.setIcon(QIcon("./src/resources/trashIcon.png"))
            self.flightsTable.setCellWidget(row, 1, botao)
            row = row + 1
    
    def showEvent(self, ev: QShowEvent) -> None:
        self.loadData()
        return super(FlightsListView, self).showEvent(ev)
