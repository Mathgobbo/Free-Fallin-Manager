from src.models.FlyingMember import FlyingMember
from src.views.signUpFlyingMemberView import SignUpFlyingMemberView


class SignUpFlyingMemberController:
    def __init__(self) -> None:
        self.__view = SignUpFlyingMemberView()
    
    def openView(self):
        self.__view = SignUpFlyingMemberView()
    
    def isEmpty(self, flyingMember):
        if flyingMember.cpf() != "" and flyingMember.name() != "" and flyingMember.phone() != "" and flyingMember.weight() != "" and flyingMember.height() != "":
            return True
        return False
    
    
