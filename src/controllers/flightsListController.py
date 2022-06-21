from src.models.Fly import Fly
from src.views.flightsListView import FlightsListView


class FlightsListController:
    def __init__(self, app) -> None:
        self.__app = app
        self.__view = FlightsListView(self)
    
    def openView(self):
        self.__view.show()