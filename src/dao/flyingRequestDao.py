
from src.models.FlyingMember import FlyingMember
from src.models.FlyingRequest import FlyingRequest
from src.dao.abstractDAO import AbstractDAO


class FlyingRequestDAO(AbstractDAO):
    def __init__(self) -> None:
        super().__init__('flyingRequest.pkl')

    def get(self, key):
        if isinstance(key, int):
            return super().get(key)

    def add(self, key, flyingRequest):
        if (flyingRequest is not None) and (isinstance(flyingRequest, FlyingRequest) and (isinstance(key, str))):
            return super().add(key, flyingRequest)

    def remove(self, key):
        if isinstance(key, int):
            return super().remove(key)

    def getAll(self):
        return super().getAll()
