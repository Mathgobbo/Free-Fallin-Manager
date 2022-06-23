

from PyQt5.QtWidgets import QApplication
from src.controllers.clientFlightsListController import ClientFlightsListController
from src.dao.flightDao import FlightDao
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
from src.controllers.flightsListController import FlightsListController
from src.controllers.flightRegistrationController import FlightRegistrationController
from src.controllers.editPlaneController import EditPlaneController
from src.controllers.editFlightController import EditFlightController


class AppController:
  def __init__(self):
    self.__app = QApplication([])
    # DAOs
    self.__adminDao = AdminDao()
    self.__planeDao = PlaneDao()
    self.__flightDao = FlightDao()

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
    self.__flightsListController = FlightsListController(self)
    self.__flightRegistrationController = FlightRegistrationController(self)
    self.__editPlaneController = EditPlaneController(self, self.__planeDao)
    self.__editFlightController = EditFlightController(self)
    self.__clientFlightsController = ClientFlightsListController(self, self.__flightDao)
  
  def start(self):
    self.__mainMenuController.openView()
    self.__app.exec_()

  def openMainMenu(self):
    self.__mainMenuController.openView()
  
  def openFlightsToBook(self):
    self.__clientFlightsController.openView()

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
  
  def openFlightsListView(self):
    self.__flightsListController.openView()
  
  def openFlightRegistrationView(self):
    self.__flightRegistrationController.openView()

  def openPlaneRegistration(self):
    self.__planeRegistrationController.openView()

  def openEditPlane(self, plane):
    self.__editPlaneController.openView(plane)
  
  def openEditFlight(self):
    self.__editFlightController.openView()

  @property
  def adminList(self):
    return self.__adminList
