
from src.models.Admin import Admin
from src.views.signUpAdminView import SignUpAdminView


class SignUpAdminController:
  def __init__(self, app) -> None:
    self.__view = SignUpAdminView(self)
    self.__app = app

  def openView(self):
    self.__view.openSignUpAdminView()
