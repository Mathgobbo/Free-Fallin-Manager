from src.models.Admin import Admin
from src.views.loginView import LoginView


class LoginController:
    def __init__(self, appController) -> None:
        self.__app = appController
        self.__view = LoginView(self)
    
    def openView(self):
        self.__view.openView()

    # Verifica se os campos estão vazios
    def isEmpty(self,admin):
        if admin.username() != "" and admin.password() != "":
            return True
        return False

    # Verifica se o login é valido
    def isValidLogin(self,admin):
        if admin.username() == "root" and admin.password() == "pass":
            return True
        return False

    # Efetua o login
    def Login(self,admin):
        if self.isEmpty(admin):
            if self.isValidLogin(admin):
                self.__app.openAdminMenu()
            else:
                self.__view.invalidUser()
        else:
            self.__view.emptyFields()

