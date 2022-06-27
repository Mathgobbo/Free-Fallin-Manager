from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QToolButton
from PyQt5.QtGui import QIcon, QShowEvent


class PlaneListView(QMainWindow):
    
    def __init__(self, controller):
        super(PlaneListView, self).__init__()
        self.__controller = controller
        uic.loadUi(r'.\src\resources\planeList.ui', self)

        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)
        self.addPlaneButton = self.findChild(QPushButton, "addPlaneButton")
        self.addPlaneButton.clicked.connect(self.openPlaneRegistration)
        self.table = self.findChild(QTableWidget, "planesTable")
        self.table.setColumnWidth(3,30)



    def showEvent(self, ev: QShowEvent) -> None:
        self.loadData()
        return super(PlaneListView, self).showEvent(ev)
    
    def backButtonClick(self):
        self.close()
        self.__controller.back()

    def openPlaneRegistration(self):
        self.__controller.goToPlaneRegistration()

    def loadData(self):
        row = 0
        planes =  self.__controller.getPlanes()
        self.table.setRowCount(len(planes))
        for plane in planes:
            nameColumn = QLabel(plane.name)
            modelColumn = QLabel(plane.model)
            capacityColumn = QLabel(str(plane.capacity_limit))
            nameColumn.mousePressEvent = self.openEditPlane(plane)
            self.table.setCellWidget(row, 0, nameColumn)
            self.table.setCellWidget(row, 1, modelColumn)
            self.table.setCellWidget(row, 2, capacityColumn)
            button = QToolButton()
            button.setIcon(QIcon("./src/resources/trashIcon.png"))
            button.clicked.connect(self.deleteButtonClick(plane))
            self.table.setCellWidget(row, 3, button)
            row = row + 1
    
    def deleteButtonClick(self, plane):
        def delete():
            self.__controller.deletePlane(plane.name)
        return delete
    
    def openEditPlane(self, plane):
        def editPlane(event):
            self.__controller.editPlane(plane)
        return editPlane