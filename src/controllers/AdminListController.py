
from src.dao.adminDao import AdminDao
from src.models.Admin import Admin
from src.views.adminListView import AdminListView


class AdminListController:
  def __init__(self, app) -> None:
    self.__app = app
    self.__dao = AdminDao()
    self.__view = AdminListView(self)

  def openView(self):
    self.__view.show()

  def back(self):
    self.__app.openAdminMenu()

  def goToSignUpAdmin(self):
    self.__view.close()
    self.__app.openSignUpAdmin()
  
  def getAdmins(self):
    return self.__dao.getAll()

