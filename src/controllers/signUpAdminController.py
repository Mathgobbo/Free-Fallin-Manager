from src.models.Admin import Admin
from src.views.signUpAdminView import SignUpAdminView


class SignUpAdminController:
  def __init__(self) -> None:
    self.__view = SignUpAdminView()

  def openView(self):
    self.__view.openSignUpAdminView()

  def isEmpty(self,admin):
      if admin.username() != "" and admin.password() != "":
          return True
      return False


  def isFormValid(self,admin):
      if admin.username() == "root" and admin.password() == "pass":
          return True
      return False

  def SignUp(self,admin):
      self.__view.openLoginView()
      if self.isEmpty(admin):
          if self.isValidLogin(admin):
              self.__view.openAdminMenu()
          else:
              print("Usuário ou senha estão incorretos!")
      else:
          print("Preencha os campos obrigatório!")