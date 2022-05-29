from src.views.membersListView import MembersListView


class MembersMenuController:
    def __init__(self, appController) -> None:
        self.__app = appController
        self.__view = MembersListView(self)
    
    def openView(self):
        self.__view.openView()
