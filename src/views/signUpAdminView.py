from PyQt5 import uic, QtWidgets


class SignUpAdminView:
    
    app = QtWidgets.QApplication([])
    view = uic.loadUi(r'.\src\resources\signUpAdmin.ui')

    def openSignUpAdminView(self):
        self.view.show()
        self.app.exec() 

