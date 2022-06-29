from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QToolButton
from PyQt5.QtGui import QIcon, QShowEvent
from src.models.Plane import Plane
from src.models.Fly import Fly

class ClientFlightsListView(QMainWindow):
    
    def __init__(self, controller):
        super(ClientFlightsListView, self).__init__()
        self.__controller = controller
        uic.loadUi(r'.\src\resources\clientFlightsList.ui', self)

        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)
        self.table = self.findChild(QTableWidget, "tableWidget")

    def showEvent(self, ev: QShowEvent) -> None:
        self.loadData()
        return super(ClientFlightsListView, self).showEvent(ev)
    
    def backButtonClick(self):
        self.close()
        self.__controller.back()

    def loadData(self):
        row = 0
        flights =  self.__controller.getFlights()
        # MOCKS! TEM QUE TROCAR MAIS TARDE
        mockedFlights = [
            Fly("15-07-2020 08:15:00", [], Plane("Roger Santos", "Patata", 1)),
            Fly("10-03-2002 18:15:00", [], Plane("Maçarico 1", "Patata", 4))
        ]

        flightsToShow = []
        for flight in flights:
            if flight.plane.capacity_limit > len(flight.members):
                flightsToShow.append(flight)

        self.table.setRowCount(len(flightsToShow))
        self.table.setColumnWidth(0,130)
        self.table.setColumnWidth(1,180)
        self.table.setColumnWidth(2,200)

        for flight in flightsToShow:
            dateTimeColumn = QLabel(str(flight.date_time.toString()))
            planeColumn = QLabel(flight.plane.name)
            capacityColumn = QLabel(str(flight.plane.capacity_limit - len(flight.members)))
            dateTimeColumn.mousePressEvent = self.nextStep(flight)
            self.table.setCellWidget(row, 0, dateTimeColumn)
            self.table.setCellWidget(row, 1, planeColumn)
            self.table.setCellWidget(row, 2, capacityColumn)
            row = row + 1
    
   
    
    def nextStep(self, flight):
        def editPlane(event):
            self.close()
            self.__controller.nextStep(flight)
        return editPlane