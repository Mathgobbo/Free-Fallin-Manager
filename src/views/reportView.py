from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QToolButton
from PyQt5.QtGui import QIcon, QShowEvent


class ReportView(QMainWindow):
    
    def __init__(self, controller):
        super(ReportView, self).__init__()
        self.__controller = controller
        uic.loadUi(r'.\src\resources\report.ui', self)

        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)
        self.filterButton = self.findChild(QPushButton, "filterButton")
        self.filterButton.clicked.connect(self.loadData)
        self.table = self.findChild(QTableWidget, "monthTable")
        self.table.setColumnWidth(3,30)
        self.averageLabel = self.findChild(QLabel, "averageLabel")
        self.averageLabel.setVisible(False)



    # def showEvent(self, ev: QShowEvent) -> None:
    #     self.loadData()
    #     return super(ReportView, self).showEvent(ev)
    
    def backButtonClick(self):
        self.close()
        self.__controller.back()

    def loadData(self):
        row = 0
        flights =  self.__controller.getFlights()
        self.table.setRowCount(len(flights))
        for flight in flights:
            mouthColumn = QLabel(flight.mouth)
            flightsColumn = QLabel(flight.model)
            self.table.setCellWidget(row, 0, mouthColumn)
            self.table.setCellWidget(row, 1, flightsColumn)
            row = row + 1
    