from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton

class AdminMenuView(QMainWindow):

    def __init__(self, controller):
        self.__controller = controller
        super(AdminMenuView, self).__init__()
        uic.loadUi(r'.\src\resources\adminMenu.ui', self)

        self.adminListButton = self.findChild(QPushButton,"admins")
        self.adminListButton.clicked.connect(self.goToAdmins)
    
        self.flyingMembersListButton = self.findChild(QPushButton,"membros_de_voo")
        self.flyingMembersListButton.clicked.connect(self.goToFlyingMembers)

        self.planeListButton = self.findChild(QPushButton,"avioes")
        self.planeListButton.clicked.connect(self.goToPlanes)

        self.flightsListButton = self.findChild(QPushButton, "voos")
        self.flightsListButton.clicked.connect(self.goToFlights)

    def openView(self):
        self.show()
    
    def goToFlyingMembers(self):
        self.close()
        self.__controller.goToFlyingMembersList()

    def goToAdmins(self):
        self.close()
        self.__controller.goToAdminList()
    
    def goToPlanes(self):
        self.close()
        self.__controller.goToPlanesList()
    
    def goToFlights(self):
        self.close()
        self.__controller.goToFlightsList()
    
    
    
    