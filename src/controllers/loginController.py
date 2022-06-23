from gettext import NullTranslations
from src.models.Admin import Admin
from src.views.loginView import LoginView
from src.controllers.AdminListController import AdminListController


class LoginController:
    def __init__(self, controller) -> None:
        self.__controller = controller
        self.__view = LoginView(self)
    
    # Abre a tela
    def openView(self):
        self.__view.openView()

    # Verifica se os campos estão vazios
    def isEmpty(self, username, password):
        if username != "" and password != "":
            return True
        return False

    # Verifica se o login é valido
    def isValidLogin(self, username, password):
        adminListController = self.__controller.adminList
        for admin in adminListController.getAdmins():
            if username == admin.username and password == admin.password:
                return True

    # Efetua o login
    def Login(self,username, password):
        if self.isEmpty(username, password):
            if self.isValidLogin(username, password):
                self.__view.close()
                self.__controller.openAdminMenu()
            else:
                self.__view.invalidUser()
        else:
            self.__view.emptyFields()

