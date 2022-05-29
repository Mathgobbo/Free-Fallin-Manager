
from src.models.Admin import Admin
from src.views.adminListView import AdminListView


class AdminListController:
  def __init__(self, app) -> None:
    self.__view = AdminListView(self)
    self.__app = app

  def openView(self):
    self.__view.show()

  def back(self):
    self.__app.openAdminMenu()

