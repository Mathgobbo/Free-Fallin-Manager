from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton

class MainMenuView(QMainWindow):

    def __init__(self, controller):
        self.__controller = controller
        super(MainMenuView, self).__init__()
        uic.loadUi(r'.\src\resources\mainMenu.ui', self)

        self.loginAdminButton = self.findChild(QPushButton,"botaoLogin")
        self.loginAdminButton.clicked.connect(self.goToSignIn)
    
        self.wannaFlyButton = self.findChild(QPushButton,"botaoSaltar")
        self.wannaFlyButton.clicked.connect(self.gotToFlightsToBook)

    def openView(self):
        self.show()
    
    
    def goToSignIn(self):
        self.close()
        self.__controller.goToSignInAdmin()
    
    def gotToFlightsToBook(self):
        self.close();
        self.__controller.goToFlightsToBook();
    
    
    
    