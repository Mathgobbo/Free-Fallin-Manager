from PyQt5 import uic, QtWidgets


class LoginView:
    app = QtWidgets.QApplication([])
    login = uic.loadUi(r'C:\free-fallin-manager\src\resources\login.ui')
    menu_admin = uic.loadUi(r'C:\free-fallin-manager\src\resources\menuAdmin.ui')

    # Abre a tela de login
    def openLoginView(self):
        self.login.show()
        self.app.exec() 

    # Abre a tela principal do admin
    def openAdminMenu(self):
        self.menu_admin.show()
        self.app.exec() 