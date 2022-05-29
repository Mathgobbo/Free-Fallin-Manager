



from src.views.adminMenuView import AdminMenuView


class AdminMenuController:
  def __init__(self, appController) -> None:
    self.__app = appController
    self.__view = AdminMenuView(self)

  def openView(self):
    self.__view.openView()

  def goToAdminList(self):
    self.__app.openAdminList()

  def goToSignUpAdmin(self):
    self.__app.openSignUpAdmin()


  

  
