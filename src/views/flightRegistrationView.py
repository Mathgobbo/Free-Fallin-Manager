from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QComboBox, QPushButton, QSpinBox, QDateEdit, QTimeEdit


class FlightRegistrationView(QMainWindow):

    def __init__(self, controller) -> None:
        super(FlightRegistrationView, self).__init__()
        uic.loadUi(r'.\src\resources\flightRegistration.ui', self)

        self.__controller = controller

        self.addMembroButton = self.findChild(QPushButton, "addMembro")
        self.addMembroButton.clicked.connect(self.goToAddMembro)

        self.dateInput = self.findChild(QDateEdit, "dateInput")

        self.timeInput = self.findChild(QTimeEdit, "timeInput")

        self.planeComboBox = self.findChild(QComboBox, "planeComboBox")

        self.membersComboBox = self.findChild(QComboBox, "membersComboBox")

    def showEvent(self, ev):

        self.planeComboBox.clear()
        for i in self.__controller.getPlanes():
            self.planeComboBox.addItem(i.name)
        
        self.membersComboBox.clear()
        for j in self.__controller.getFlyMembers():
            self.membersComboBox.addItem(j.name, j.type)

        return super(FlightRegistrationView, self).showEvent(ev)
    
    def openFlightRegistrationView(self):
        self.show()
    
    def goToAddMembro(self):
        self.close()
        self.__controller.goToAddMember()
    