
from models.Administrator import Admin
from src.dao.abstractDAO import AbstractDAO


class AdminDao(AbstractDAO):
    def __init__(self) -> None:
        super().__init__('admin.pkl')

    def get(self, key):
        if isinstance(key, str):
            return super().get(key)

    def add(self, username, admin):
        if (admin is not None) and (isinstance(admin, Admin) and (isinstance(username, str))):
            return super().add(username, admin)

    def remove(self, key):
        if isinstance(key, str):
            return super().remove(key)

    def update(self, username, admin):
        super().remove(username)
        super().add(admin.username, admin)
        return

    def getAll(self):
        return super().getAll()
