

from PyQt5.QtWidgets import QApplication
from src.controllers.AdminListController import AdminListController
from src.controllers.adminMenuController import AdminMenuController
from src.controllers.signUpAdminController import SignUpAdminController
from src.controllers.mainMenuController import MainMenuController

class AppController:
  def __init__(self):
    self.__app = QApplication([])
    self.__mainMenuController = MainMenuController(self)
    self.__signUpAdminController = SignUpAdminController(self)
    self.__adminMenuController = AdminMenuController(self)
    self.__adminList = AdminListController(self)

  
  def start(self):
    self.__mainMenuController.openView()
    self.__app.exec_()

  def openSignUpAdmin(self):
    self.__signUpAdminController.openView()

  def openAdminMenu(self):
    self.__adminMenuController.openView()

  def openAdminList(self):
    self.__adminList.openView()