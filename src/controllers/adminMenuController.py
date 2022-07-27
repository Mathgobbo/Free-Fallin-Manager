



from src.views.adminMenuView import AdminMenuView


class AdminMenuController:
  def __init__(self, appController) -> None:
    self.__app = appController
    self.__view = AdminMenuView(self)

  def openView(self):
    self.__view.openView()

  def goToAdminList(self):
    self.__app.openAdminList()

  def goToFlyingMembersList(self):
    self.__app.openFlyingMembersListView()

  def goToSignUpAdmin(self):
    self.__app.openSignUpAdmin()

  def goToPlanesList(self):
    self.__app.openPlaneList()
  
  def goToFlightsList(self):
    self.__app.openFlightsListView()
  
  def goToFlightsRequestApprovalList(self):
    self.__app.openFlightsRequestsApprovalList()

  def goToReportView(self):
    self.__app.openReportView()