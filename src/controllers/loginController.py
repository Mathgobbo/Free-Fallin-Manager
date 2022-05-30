from gettext import NullTranslations
from src.models.Admin import Admin
from src.views.loginView import LoginView


class LoginController:
    def __init__(self, appController) -> None:
        self.__app = appController
        self.__view = LoginView(self)
    
    # Abre a tela
    def openView(self):
        self.__view.openView()

    # Verifica se os campos estão vazios
    def isEmpty(self,Admin):
        if Admin.username != "" and Admin.password != "":
            return True
        return False

    # Verifica se o login é valido
    def isValidLogin(self,Admin):
        if Admin.username == "root" and Admin.password == "pass":
            return True
        return False

    # Efetua o login
    def Login(self,username, password):
        newAdmin = Admin(username, password)
        if self.isEmpty(newAdmin):
            if self.isValidLogin(newAdmin):
                self.__view.close()
                self.__app.openAdminMenu()
            else:
                self.__view.invalidUser()
        else:
            self.__view.emptyFields()

