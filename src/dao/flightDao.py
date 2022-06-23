


from src.models.Fly import Fly
from src.dao.abstractDAO import AbstractDAO


class FlightDao(AbstractDAO):
    def __init__(self) -> None:
        super().__init__('flights.pkl')

    def get(self, key):
        if isinstance(key, str):
            return super().get(key)

    def add(self, name, flight):
        if (flight is not None) and (isinstance(flight, Fly) and (isinstance(name, str))):
            return super().add(name, flight)

    def remove(self, key):
        if isinstance(key, str):
            return super().remove(key)

    def update(self, name, flight):
        super().remove(name)
        super().add(flight.name, flight)
        return

    def getAll(self):
        return super().getAll()
