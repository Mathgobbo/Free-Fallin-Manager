from src.views.membersListView import MembersListView


class FlyingMembersMenuController:
    def __init__(self, appController) -> None:
        self.__app = appController
        self.__view = MembersListView(self)
    
    def openView(self):
        self.__view.openView()

    def goToAddMember(self):
        self.__app.openAddMemberView()
    
    def back(self):
        self.__app.openAdminMenu()
