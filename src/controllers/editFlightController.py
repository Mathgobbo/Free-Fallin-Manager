from src.models.Fly import Fly
from src.views.editFlightView import EditFlightView


class EditFlightController:
    def __init__(self, app) -> None:
        self.__app = app
        self.__view = EditFlightView(self)
    
    def openView(self):
        self.__view.openEditFlightView()
    
    def atualizarVoo(self):
        pass

    def goToFlightList(self):
        self.__app.openFlightsListView()
        