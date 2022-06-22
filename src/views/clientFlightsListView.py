from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QToolButton
from PyQt5.QtGui import QIcon, QShowEvent


class ClientFlightsListView(QMainWindow):
    
    def __init__(self, controller):
        super(ClientFlightsListView, self).__init__()
        self.__controller = controller
        uic.loadUi(r'.\src\resources\clientFlightsList.ui', self)

        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)
        self.table = self.findChild(QTableWidget, "tableWidget")
        self.table.setColumnWidth(3,30)

    def showEvent(self, ev: QShowEvent) -> None:
        self.loadData()
        return super(ClientFlightsListView, self).showEvent(ev)
    
    def backButtonClick(self):
        self.close()
        self.__controller.back()

    def loadData(self):
        row = 0
        flights =  self.__controller.getFlights()
        self.table.setRowCount(len(flights))
        for flight in flights:
            dateTimeColumn = QLabel(flight.date_time)
            planeColumn = QLabel(flight.plane.name)
            capacityColumn = QLabel(flight.plane.capacity_limit - len(flight.members))
            dateTimeColumn.mousePressEvent = self.nextStep(flight)
            self.table.setCellWidget(row, 0, dateTimeColumn)
            self.table.setCellWidget(row, 1, planeColumn)
            self.table.setCellWidget(row, 2, capacityColumn)
            row = row + 1
    
   
    
    def nextStep(self, flight):
        def editPlane(event):
            self.__controller.nextStep(flight)
        return editPlane