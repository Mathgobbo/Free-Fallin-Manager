
from src.models.FlyingMember import FlyingMember
from src.dao.abstractDAO import AbstractDAO


class FlyingMemberDAO(AbstractDAO):
    def __init__(self) -> None:
        super().__init__('members.pkl')

    def get(self, key):
        # Mudei para str
        if isinstance(key, str):
            return super().get(key)

    def add(self, cpf, member):
        if (member is not None) and (isinstance(member, FlyingMember) and (isinstance(cpf, str))):
            return super().add(cpf, member)

    def remove(self, key):
        # Mudei key para str
        if isinstance(key, str):
            return super().remove(key)

    def getAll(self):
        return super().getAll()
    
    def update(self, cpf, member):
        super().remove(cpf)
        super().add(member.cpf, member)
        return
