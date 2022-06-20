class PlaneRegistrationController:
    def __init__(self, app, planeDao) -> None:
        #self.__view = PlaneRegistrationView(self)
        self.__dao = planeDao
        self.__app = app

    def openView(self):
        self.__view.show()
    
    def back(self):
        self.__view.close()
        self.__app.openPlaneList()

    def signUp(self):
        isValid = self.isFormValid()
        if(not isValid): 
            return
        
        newAdmin = Admin(self.__view.usernameInput.text(), self.__view.passInput.text())
        self.__dao.add(self.__view.usernameInput.text(),newAdmin)
        self.back()
        self.__view.clearInputs()

    def isFormValid(self): 
        isValid = True
        self.__view.usernameError.setText("")
        self.__view.passError.setText("")
        self.__view.confirmPassError.setText("")
        
        if(self.__view.usernameInput.text() == ""):
            self.__view.usernameError.setText("Insira um Nome de Usuário")
            isValid =  False
        if(self.__view.passInput.text() == ""):
            self.__view.passError.setText("Insira uma Senha")
            isValid =  False
        if(self.__view.confirmPassInput.text() == ""):
            self.__view.confirmPassError.setText("Confirme a senha informada")
            isValid =  False
        if(self.__view.confirmPassInput.text() != self.__view.passInput.text()):
            self.__view.confirmPassError.setText("Confirmação de Senha está diferente da senha informada")
            isValid =  False

        admins = self.__dao.getAll()
        for admin in admins:
            if admin.username ==  self.__view.usernameInput.text():
                self.__view.usernameError.setText("Já existe um Administrador com este nome de Usuário!")
                isValid =  False
                break
            return isValid