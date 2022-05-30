
from src.models.FlyingMember import FlyingMember
from src.dao.abstractDAO import AbstractDAO


class FlyingMemberDAO(AbstractDAO):
    def __init__(self) -> None:
        super().__init__('members.pkl')

    def get(self, key):
        if isinstance(key, int):
            return super().get(key)

    def add(self, cpf, member):
        if (member is not None) and (isinstance(member, FlyingMember) and (isinstance(cpf, str))):
            return super().add(cpf, member)

    def remove(self, key):
        if isinstance(key, int):
            return super().remove(key)

    def getAll(self):
        return super().getAll()
