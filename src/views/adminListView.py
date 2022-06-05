from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QToolButton
from PyQt5.QtGui import QIcon, QShowEvent


class AdminListView(QMainWindow):
    
    def __init__(self, controller):
        super(AdminListView, self).__init__()
        self.__controller = controller
        uic.loadUi(r'.\src\resources\adminList.ui', self)

        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)
        self.addAdminButton = self.findChild(QPushButton, "addAdminButton")
        self.addAdminButton.clicked.connect(self.openSignUpAdmin)
        self.table = self.findChild(QTableWidget, "adminsTable")
        self.table.setColumnWidth(0,300)


    def showEvent(self, ev: QShowEvent) -> None:
        self.loadData()
        return super(AdminListView, self).showEvent(ev)
   

    def openSignUpAdminView(self):
        self.__controller
    
    def backButtonClick(self):
        self.close()
        self.__controller.back()

    def openSignUpAdmin(self):
        self.__controller.goToSignUpAdmin()

    def loadData(self):
        row = 0
        admins =  self.__controller.getAdmins()
        self.table.setRowCount(len(admins))
        for admin in admins:
            usernameColumn = QLabel(admin.username)
            usernameColumn.mousePressEvent = self.openEditAdmin(admin)
            self.table.setCellWidget(row, 0, usernameColumn)
            button = QToolButton()
            button.setIcon(QIcon("./src/resources/trashIcon.png"))
            button.clicked.connect(self.deleteGenerator(admin))
            self.table.setCellWidget(row, 1, button)
            row = row + 1
    
    def deleteGenerator(self, admin):
        def delete():
            self.__controller.deleteAdmin(admin.username)
            self.loadData()
        return delete
    
    def openEditAdmin(self, admin):
        def editAdmin(event):
            self.__controller.editAdmin(admin)
        return editAdmin