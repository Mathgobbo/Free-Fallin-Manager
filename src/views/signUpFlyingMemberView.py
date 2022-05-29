from PyQt5 import uic, QtWidgets


class SignUpFlyingMemberView:

    app = QtWidgets.QApplication([])
    view = uic.loadUi(r'.\src\resources\signUpFlyingMember.ui')

    def openSignUpFlyingMemberView(self):
        self.view.show()
        self.app.exec()
