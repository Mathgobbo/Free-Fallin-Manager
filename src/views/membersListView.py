from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QShowEvent


class MembersListView(QMainWindow):
    def __init__(self, controller):
        super(MembersListView, self).__init__()
        uic.loadUi(r'.\src\resources\listingMembers.ui', self)
        self.__controller = controller

        self.addMemberButton = self.findChild(QPushButton, "addMemberButton")
        self.addMemberButton.clicked.connect(self.goToAddMember)

        self.voltar = self.findChild(QPushButton, "voltar")
        self.voltar.clicked.connect(self.voltarClick)

    def openView(self):
        self.show()
    
    def goToAddMember(self):
        self.__controller.goToAddMember()
    
    def voltarClick(self):
        self.close()
        self.__controller.back()
    
    def loadData(self):
        flyMembers = self.__controller.getMembers()
    
    def showEvent(self, ev: QShowEvent) -> None:
        self.loadData()
        return super(MembersListView, self).showEvent(ev)
