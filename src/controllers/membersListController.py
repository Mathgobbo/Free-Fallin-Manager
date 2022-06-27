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
