

from PyQt5.QtWidgets import QApplication
from src.dao.adminDao import AdminDao
from src.controllers.signUpFlyingMemberController import SignUpFlyingMemberController
from src.controllers.flyingMembersMenuController import FlyingMembersMenuController
from src.controllers.loginController import LoginController
from src.controllers.adminListController import AdminListController
from src.controllers.adminMenuController import AdminMenuController
from src.controllers.signUpAdminController import SignUpAdminController
from src.controllers.mainMenuController import MainMenuController

class AppController:
  def __init__(self):
    self.__app = QApplication([])
    # DAOs
    self.__adminDao = AdminDao()
    self.__mainMenuController = MainMenuController(self)
    self.__adminMenuController = AdminMenuController(self)
    self.__adminList = AdminListController(self, self.__adminDao)
    self.__signUpAdminController = SignUpAdminController(self, self.__adminDao)
    self.__loginController = LoginController(self)
    self.__flyingMembersController = FlyingMembersMenuController(self)
    self.__signUpFlyingMemberController = SignUpFlyingMemberController(self)
  
  def start(self):
    self.__mainMenuController.openView()
    self.__app.exec_()

  def openSignUpAdmin(self):
    self.__signUpAdminController.openView()

  def openAdminMenu(self):
    self.__adminMenuController.openView()

  def openAdminList(self):
    self.__adminList.openView()
  
  def openLoginView(self):
    self.__loginController.openView()
  
  def openFlyingMembersListView(self):
    self.__flyingMembersController.openView()

  def openAddMemberView(self):
    self.__signUpFlyingMemberController.openView()
