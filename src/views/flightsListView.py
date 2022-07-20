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
        self.close()
        self.__controller.goToAddFlight()
    
    def botaoVoltarClick(self):
        self.close()
        self.__controller.back()
    
    def loadData(self):
        row = 0
        flights = self.__controller.getFlights()
        self.flightsTable.setRowCount(len(flights))

        for flight in flights:
            dateTime = QLabel(str(flight.date_time.toString()))
            self.flightsTable.setCellWidget(row, 0, dateTime)
            dateTime.mousePressEvent = self.openEditFlight(flight)
            plane = QLabel(flight.plane.name)
            self.flightsTable.setCellWidget(row, 1, plane)
  
            capacityColumn = QLabel(str(flight.plane.capacity_limit - len(flight.members)))
            self.flightsTable.setCellWidget(row, 2, capacityColumn)
            
            botao = QToolButton()
            botao.setIcon(QIcon("./src/resources/trashIcon.png"))
            botao.clicked.connect(self.deleteButtonClick(flight))
            self.flightsTable.setCellWidget(row, 3, botao)
            row = row + 1
    
    def showEvent(self, ev: QShowEvent) -> None:
        self.loadData()
        return super(FlightsListView, self).showEvent(ev)
    
    def openEditFlight(self, flight):
        def editFlight(event):
            self.__controller.editarVoo(flight)
        return editFlight

    def deleteButtonClick(self, flight):
        def delete():
            self.__controller.deleteFlight(str(flight.date_time))
            self.loadData()
        return delete
    
