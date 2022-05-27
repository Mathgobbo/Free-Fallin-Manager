from PyQt5 import uic, QtWidgets

class View(): 
    app=QtWidgets.QApplication([])
    login=uic.loadUi(r'C:\free-fallin-manager\src\resources\login.ui')
    menu_admin = uic.loadUi(r'C:\free-fallin-manager\src\resources\menuAdmin.ui')
    main_menu=uic.loadUi(r'C:\free-fallin-manager\src\resources\mainMenu.ui')

    # Abre a tela de login
    def abrir_tela_login(self):
        self.login.show()
        self.app.exec() 

    # Abre a tela inicial
    def abrir_cadastro_professor(self):
        self.main_menu.show()
        self.app.exec() 
    
     # Abre a tela principal do admin
    def abrir_area_logada(self):
        self.menu_admin.show()
        self.app.exec() 

v = View()

# Abrir tela de Login:
#v.abrir_tela_login()
# Abrir tela de area logada: 
#v.abrir_area_logada()
# Abrir tela de cadastro de professor: 
v.abrir_cadastro_professor()
