from gettext import NullTranslations
from src.models.Administrator import Admin
from src.views.loginView import LoginView
from src.controllers.AdminListController import AdminListController


class LoginController:
    def __init__(self, appController) -> None:
        self.__app = appController
        self.__view = LoginView(self)
    
    # Abre a tela
    def openView(self):
        self.__view.openView()

    # Verifica se os campos estão vazios
    def isEmpty(self, username, password):
        newAdmin = Admin(username, password)
        if newAdmin.username != "" and newAdmin.password != "":
            return True
        return False

    # Verifica se o login é valido
    def isValidLogin(self, username, password):
        adminListController = self.__app.adminList
        newAdmin = Admin(username, password)
        for admin in adminListController.getAdmins():
            if newAdmin.username == admin.username and newAdmin.password == admin.password:
                return True


    # Efetua o login
    def Login(self,username, password):
        if self.isEmpty(username, password):
            if self.isValidLogin(username, password):
                self.__view.close()
                self.__app.openAdminMenu()
            else:
                self.__view.invalidUser()
        else:
            self.__view.emptyFields()

