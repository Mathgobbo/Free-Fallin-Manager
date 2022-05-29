

from PyQt5.QtWidgets import QApplication
from src.controllers.signUpAdminController import SignUpAdminController
from src.controllers.mainMenuController import MainMenuController

class AppController:
  def __init__(self):
    self.__app = QApplication([])
    self.__mainMenuController = MainMenuController(self)
    self.__signUpAdminController = SignUpAdminController(self)

  
  def start(self):
    self.__mainMenuController.openView()
    self.__app.exec_()

  def openSignUpAdmin(self):
    self.__signUpAdminController.openView()