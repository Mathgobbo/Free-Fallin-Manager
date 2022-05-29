


from src.views.mainMenuView import MainMenuView


class MainMenuController:
  def __init__(self, appController) -> None:
    self.__app = appController
    self.__view = MainMenuView(self)

  def openView(self):
    self.__view.openView()

  def goToSignUpAdmin(self):
    self.__app.openSignUpAdmin()


  

  
