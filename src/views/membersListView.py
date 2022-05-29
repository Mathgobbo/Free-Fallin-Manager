from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel

from src.models.FlyingMember import FlyingMember


class MembersListView(QMainWindow):
    def __init__(self, controller):
        self.__controller = controller
        super(MembersListView, self).__init__()
        uic.loadUi(r'.\src\resources\listingMembers.ui', self)
    
    def openView(self):
        self.show()
    
