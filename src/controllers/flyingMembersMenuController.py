from src.views.membersListView import MembersListView
from src.dao.flyingMemberDao import FlyingMemberDAO


class FlyingMembersMenuController:
    def __init__(self, appController, flyMemberDao) -> None:
        self.__app = appController
        self.__dao = flyMemberDao
        self.__view = MembersListView(self)
    
    def openView(self):
        self.__view.openView()

    def goToAddMember(self):
        self.__app.openAddMemberView()
    
    def back(self):
        self.__app.openAdminMenu()
    
    def getMembers(self):
        return self.__dao.getAll()
