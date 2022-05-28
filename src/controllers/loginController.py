from src.models.Admin import Admin
from src.views.loginView import LoginView


class loginController:

    def __init__(self):
        admin = Admin()
        view = LoginView()
    
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
        self.view.openLoginView()

        if self.isEmpty(admin):
            if self.isValidLogin(admin):
                self.view.openAdminMenu()
            else:
                print("Usuário ou senha estão incorretos!")
        else:
            print("Preencha os campos obrigatório!")

