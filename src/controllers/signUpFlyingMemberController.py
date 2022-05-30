from src.models.FlyingMember import FlyingMember
from src.views.signUpFlyingMemberView import SignUpFlyingMemberView

class SignUpFlyingMemberController:
    def __init__(self, app) -> None:
        self.__app = app
        self.__view = SignUpFlyingMemberView(self)

    def openView(self):
        self.__view.show()
    
    def isEmpty(self, flyingMember):
        if flyingMember.cpf() != "" and flyingMember.name() != "" and flyingMember.phone() != "" and flyingMember.weight() != "" and flyingMember.height() != "":
            return True
        return False
    
    # Principal!
    def signUp(self):
        isValid = self.isFormValid()
        if (not isValid):
            return
        
        # Ta faltando o tipo
        # Ver como vem o Tipo la do ComboBox pra adicionar abaixo
        newFlyingMember = FlyingMember(self.__view.cpfInput.text(), self.__view.nameInput.text(), self.__view.phoneInput.text(), self.__view.typeInput.currentData(), self.__view.weight.text(), self.__view.heightInput.text())

        # Pickle: Serializar membro

        # Sucesso? 
        #   - Voltar pra Lista com o novo membro já na lista
        #   - Mostrar menmsagem de sucesso na tela
    
    def isFormValid(self):
        isValid = True

        self.view.cpfError.setText("")
        self.view.nameError.setText("")
        self.view.phoneError.setText("")
        self.view.weight.setText("")
        self.view.height.setText("")

        if(self.view.cpfInput.text() == ""):
            self.view.cpfError.setText("Insira seu CPF")
            isValid =  False
        
        if(self.view.nameInput.text() == ""):
            self.view.nameError.setText("Insira seu Nome")
            isValid =  False
        
        if(self.view.phoneInput.text() == ""):
            self.view.phoneError.setText("Insira seu número de telefone")
            isValid =  False
        
        if(self.view.weightInput.text() == ""):
            self.view.weightError.setText("Insira seu peso")
            isValid =  False
        
        if(self.view.heightInput.text() == ""):
            self.view.heightError.setText("Insira sua altura")
            isValid =  False
        
        return isValid
