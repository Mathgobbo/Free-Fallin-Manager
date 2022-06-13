
from src.dao.adminDao import AdminDao
from models.Administrator import Admin
from src.views.editAdminView import EditAdminView


class EditAdminController:
  def __init__(self, app, adminDao) -> None:
    self.__view = EditAdminView(self)
    self.__dao = adminDao
    self.__app = app
    self.__selectedAdmin = None

  def openView(self, admin):
    self.__selectedAdmin = admin
    self.__view.openEditAdminView(admin)
  
  def back(self):
    self.__view.close()
    self.__app.openAdminList()

  def save(self):
    isValid = self.isFormValid()
    if(not isValid): 
        return
    
    newAdmin = Admin(self.__view.usernameInput.text(), self.__view.passInput.text())
    self.__dao.update(self.__selectedAdmin.username,newAdmin)
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
      if self.__selectedAdmin != admin.username and admin.username ==  self.__view.usernameInput.text():
        self.__view.usernameError.setText("Já existe um Administrador com este nome de Usuário!")
        isValid =  False
        break
    return isValid
    