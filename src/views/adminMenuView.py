from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton

class AdminMenuView(QMainWindow):

    def __init__(self, controller):
        self.__controller = controller
        super(AdminMenuView, self).__init__()
        uic.loadUi(r'.\src\resources\adminMenu.ui', self)

        self.adminListButton = self.findChild(QPushButton,"admins")
        self.adminListButton.clicked.connect(self.goToAdmins)
    

    def openView(self):
        self.show()
    
    
    def goToAdmins(self):
        self.close()
        self.__controller.goToAdminList()
    
    
    
    