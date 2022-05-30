from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel

from src.models.FlyingMember import FlyingMember


class MembersListView(QMainWindow):
    def __init__(self, controller):
        super(MembersListView, self).__init__()
        uic.loadUi(r'.\src\resources\listingMembers.ui', self)
        self.__controller = controller
        self.addMemberButton = self.findChild(QPushButton, "addMemberButton")
        self.addMemberButton.clicked.connect(self.goToAddMember)

    
    def openView(self):
        self.show()
    
    def goToAddMember(self):
        self.__controller.goToAddMember()
