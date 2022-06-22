from src.models.Fly import Fly
from src.views.editFlightView import EditFlightView


class EditFlightController:
    def __init__(self, app) -> None:
        self.__view = EditFlightView(self)
        self.__app = app
    
    def openView(self):
        self.__view.openEditFlightView()
