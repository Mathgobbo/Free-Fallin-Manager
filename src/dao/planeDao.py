from src.models.Plane import Plane
from src.dao.abstractDAO import AbstractDAO


class PlaneDao(AbstractDAO):
    def __init__(self) -> None:
        super().__init__('plane.pkl')

    def get(self, key):
        if isinstance(key, str):
            return super().get(key)

    def add(self, name, plane):
        if (plane is not None) and (isinstance(plane, Plane) and (isinstance(name, str))):
            return super().add(name, Plane)

    def remove(self, key):
        if isinstance(key, str):
            return super().remove(key)

    def update(self, name, plane):
        super().remove(name)
        super().add(plane.name, plane)
        return

    def getAll(self):
        return super().getAll()
