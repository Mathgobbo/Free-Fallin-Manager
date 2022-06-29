from src.models.Fly import Fly
from src.views.editFlightView import EditFlightView
from src.dao.flightDao import FlightDao


class EditFlightController:
    def __init__(self, app, flightDao) -> None:
        self.__view = EditFlightView(self)
        self.__app = app
        self.__flightDao = flightDao
        self.__selectedFlight = None
    
    def openView(self, flight):
        self.__selectedFlight = flight
        self.__view.openEditFlightView(flight)
    
    def atualizarVoo(self):
        print("Teste!")

    def goToFlightList(self):
        self.__app.openFlightsListView()
        