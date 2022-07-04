from src.models.FlyingMember import FlyingMember
from src.views.membersListView import MembersListView
from src.dao.flyingMemberDao import FlyingMemberDAO


class MembersListController:
    def __init__(self, app, flyMemberDao) -> None:
        self.__app = app
        self.__dao = flyMemberDao
        self.__view = MembersListView(self)

    def openView(self):
        self.__view.show()

    def goToAddMember(self):
        self.__app.openAddMemberView()
    
    def back(self):
        self.__app.openAdminMenu()
    
    def getMembers(self):
        return self.__dao.getAll()

    def deleteMember(self, cpf):
        self.__dao.remove(cpf)

    def editMember(self, member):
        self.__view.close()
        self.__app.openEditMember(member)
