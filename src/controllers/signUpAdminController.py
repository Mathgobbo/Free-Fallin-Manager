
from src.dao.adminDao import AdminDao
from src.models.Admin import Admin
from src.views.signUpAdminView import SignUpAdminView


class SignUpAdminController:
  def __init__(self, app) -> None:
    self.__view = SignUpAdminView(self)
    self.__dao = AdminDao()
    self.__app = app

  def openView(self):
    self.__view.openSignUpAdminView()
  
  def back(self):
    self.__app.openAdminList()

  def signUp(self):
    isValid = self.isFormValid()
    if(not isValid): 
        return
    
    newAdmin = Admin(self.__view.usernameInput.text(), self.__view.passInput.text())
    self.__dao.add(self.__view.usernameInput.text(),newAdmin)
    self.back()
    print(newAdmin)

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
    return isValid
    