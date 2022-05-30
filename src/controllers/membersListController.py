from src.models.FlyingMember import FlyingMember
from src.views.membersListView import MembersListView


class MembersListController:
    def __init__(self, app) -> None:
        self.__view = MembersListView(self)
        self.__app = app
    
    def openView(self):
        self.__view.show()

    def goToAddMember(self):
        self.__app.openAddMemberView()
    