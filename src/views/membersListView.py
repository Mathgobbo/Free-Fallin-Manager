from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QTableWidget, QToolButton
from PyQt5.QtGui import QIcon, QShowEvent


class MembersListView(QMainWindow):
    def __init__(self, controller):
        super(MembersListView, self).__init__()
        self.__controller = controller
        uic.loadUi(r'.\src\resources\listingMembers.ui', self)

        self.addMemberButton = self.findChild(QPushButton, "addMemberButton")
        self.addMemberButton.clicked.connect(self.goToAddMember)

        self.voltar = self.findChild(QPushButton, "voltar")
        self.voltar.clicked.connect(self.voltarClick)

        self.membersTable = self.findChild(QTableWidget, "membersTable")
        self.membersTable.setColumnWidth(0, 300)

    def openView(self):
        self.show()
    
    def goToAddMember(self):
        self.close()
        self.__controller.goToAddMember()
    
    def voltarClick(self):
        self.close()
        self.__controller.back()
    
    def loadData(self):
        row = 0
        members = self.__controller.getMembers()
        self.membersTable.setRowCount(len(members))

        for member in members:
            cpfColumn = QLabel(member.cpf)
            cpfColumn.mousePressEvent = self.openEditMember(member)

            self.membersTable.setCellWidget(row, 0, cpfColumn)

            nameColumn = QLabel(member.name)
            self.membersTable.setCellWidget(row, 1, nameColumn)

            phoneColumn = QLabel(member.phone)
            self.membersTable.setCellWidget(row, 2, phoneColumn)

            functionColumn = QLabel(str(member.type))
            self.membersTable.setCellWidget(row, 3, functionColumn)

            button = QToolButton()
            button.setIcon(QIcon("./src/resources/trashIcon.png"))
            button.clicked.connect(self.deleteButtonClick(member))
            self.membersTable.setCellWidget(row, 4, button)

            row = row + 1

    def showEvent(self, ev: QShowEvent) -> None:
        self.loadData()
        return super(MembersListView, self).showEvent(ev)
    
    def deleteButtonClick(self, member):
        def delete():
            self.__controller.deleteMember(member.cpf)
            self.loadData()
        return delete
    
    def openEditMember(self, member):
        def editMember(event):
            self.__controller.editMember(member)
        return editMember
