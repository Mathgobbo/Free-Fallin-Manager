


from src.views.clientFlightSuccessView import ClientFlightSuccessView


class ClientFlightSuccessController: 
  
    def __init__(self, app) -> None:
        self.__app = app
        self.__view = ClientFlightSuccessView(self)

    def openView(self):
        self.__view.show()

    def back(self):
        self.__app.openMainMenu()