from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QComboBox, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QToolButton
from PyQt5.QtGui import QIcon, QShowEvent
from src.models.Plane import Plane
from src.models.Fly import Fly

class FlightRequestApprovalFormView(QMainWindow):
    
    def __init__(self, controller):
        super(FlightRequestApprovalFormView, self).__init__()
        self.__controller = controller
        uic.loadUi(r'.\src\resources\flightRequestApprovalForm.ui', self)

        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)

        self.acceptButton = self.findChild(QPushButton, "acceptButton")
        self.rejectButton = self.findChild(QPushButton, "rejectButton")
        self.addMemberButton = self.findChild(QPushButton, "addMemberButton")
        self.tableInstrutores = self.findChild(QTableWidget, "tableInstrutores")
        self.membersComboBox = self.findChild(QComboBox, "membersComboBox")
        
    def showEvent(self, ev: QShowEvent) -> None:
        self.loadData()
        return super(FlightRequestApprovalFormView, self).showEvent(ev)
    
    def backButtonClick(self):
        self.close()
        self.__controller.back()

    def loadData(self):
        selectedFlightRequest =  self.__controller.getSelectedFlightRequest()
        instructors = self.__controller.getInstructors()
        print(instructors)
        for instructor in instructors:
            self.membersComboBox.addItem(instructor.name + " - " + instructor.type)

        self.flightDate = self.findChild(QLabel, "flightDate")
        self.flightDate.setText(str(selectedFlightRequest.fly.date_time.toString()))
        
        self.flightPlane = self.findChild(QLabel, "flightPlane")
        self.flightPlane.setText(selectedFlightRequest.fly.plane.name)

        self.freePlaces = self.findChild(QLabel, "freePlaces")
        self.freePlaces.setText("Lugares Disponíveis: "+str(selectedFlightRequest.fly.plane.capacity_limit - len(selectedFlightRequest.fly.members)))
        
        self.customerName = self.findChild(QLabel, "customerName")
        self.customerName.setText(selectedFlightRequest.user.name)

        self.customerDocument = self.findChild(QLabel, "customerDocument")
        self.customerDocument.setText("CPF: "+selectedFlightRequest.user.cpf)

        self.customerPhone = self.findChild(QLabel, "customerPhone")
        self.customerPhone.setText(selectedFlightRequest.user.phone)

        self.customerWeight = self.findChild(QLabel, "customerWeight")
        self.customerWeight.setText("Peso: "+str(selectedFlightRequest.user.weight)+" Kg")

        self.customerHeight = self.findChild(QLabel, "customerHeight")
        self.customerHeight.setText("Altura: "+str(selectedFlightRequest.user.height)+" Cm")
