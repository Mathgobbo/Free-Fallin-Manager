from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QToolButton
from PyQt5.QtGui import QIcon, QShowEvent
from src.models.Plane import Plane
from src.models.Fly import Fly

class FlightRequestApprovalListView(QMainWindow):
    
    def __init__(self, controller):
        super(FlightRequestApprovalListView, self).__init__()
        self.__controller = controller
        uic.loadUi(r'.\src\resources\flightResquestApprovalList.ui', self)

        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)
        self.table = self.findChild(QTableWidget, "tableWidget")

    def showEvent(self, ev: QShowEvent) -> None:
        self.loadData()
        return super(FlightRequestApprovalListView, self).showEvent(ev)
    
    def backButtonClick(self):
        self.close()
        self.__controller.back()

    def loadData(self):
        row = 0
        flightRequests =  self.__controller.getFlightRequests()
        self.table.setRowCount(len(flightRequests))
        self.table.setColumnWidth(0,130)
        self.table.setColumnWidth(1,180)
        self.table.setColumnWidth(2,200)

        for flightRequest in flightRequests:
            dateTimeColumn = QLabel(str(flightRequest.fly.date_time.toString()))
            planeColumn = QLabel(flightRequest.fly.plane.name)
            capacityColumn = QLabel(str(flightRequest.fly.plane.capacity_limit - len(flightRequest.fly.members)))
            customerColumn = QLabel(str(flightRequest.user.name))
            dateTimeColumn.mousePressEvent = self.nextStep(flightRequest)
            self.table.setCellWidget(row, 0, dateTimeColumn)
            self.table.setCellWidget(row, 1, planeColumn)
            self.table.setCellWidget(row, 2, capacityColumn)
            self.table.setCellWidget(row, 3, customerColumn)
            row = row + 1
    
   
    
    def nextStep(self, flightRequest):
        def goToApprovalScreen(event):
            self.close()
            self.__controller.nextStep(flightRequest)
        return goToApprovalScreen