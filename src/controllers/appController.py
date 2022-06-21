

from PyQt5.QtWidgets import QApplication
from src.dao.planeDao import PlaneDao
from src.controllers.planeListController import PlaneListController
from src.controllers.planeRegistrationController import PlaneRegistrationController
from src.controllers.editAdminController import EditAdminController
from src.dao.adminDao import AdminDao
from src.controllers.signUpFlyingMemberController import SignUpFlyingMemberController
from src.controllers.flyingMembersMenuController import FlyingMembersMenuController
from src.controllers.loginController import LoginController
from src.controllers.AdminListController import AdminListController
from src.controllers.adminMenuController import AdminMenuController
from src.controllers.signUpAdminController import SignUpAdminController
from src.controllers.mainMenuController import MainMenuController

class AppController:
  def __init__(self):
    self.__app = QApplication([])
    # DAOs
    self.__adminDao = AdminDao()
    self.__planeDao = PlaneDao()

    # CONTROLLERS
    self.__mainMenuController = MainMenuController(self)
    self.__adminMenuController = AdminMenuController(self)
    self.__adminList = AdminListController(self, self.__adminDao)
    self.__signUpAdminController = SignUpAdminController(self, self.__adminDao)
    self.__editAdminController = EditAdminController(self, self.__adminDao)
    self.__loginController = LoginController(self)
    self.__flyingMembersController = FlyingMembersMenuController(self)
    self.__signUpFlyingMemberController = SignUpFlyingMemberController(self)
    self.__planeListController = PlaneListController(self, self.__planeDao)
    self.__planeRegistrationController = PlaneRegistrationController(self, self.__planeDao)
  
  def start(self):
    self.__mainMenuController.openView()
    self.__app.exec_()

  def openSignUpAdmin(self):
    self.__signUpAdminController.openView()
  
  def openEditAdmin(self, admin):
    self.__editAdminController.openView(admin)

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

  def openPlaneList(self):
    self.__planeListController.openView()

  def openPlaneRegistration(self):
    self.__planeRegistrationController.openView()

  @property
  def adminList(self):
    return self.__adminList
