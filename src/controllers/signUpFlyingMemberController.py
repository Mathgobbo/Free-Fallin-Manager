from src.models.FlyingMember import FlyingMember
from src.views.signUpFlyingMemberView import SignUpFlyingMemberView
from src.dao.flyingMemberDao import FlyingMemberDAO

class SignUpFlyingMemberController:
    def __init__(self, app, flyingMemberDao) -> None:
        self.__app = app
        self.__flyingMemberDAO = flyingMemberDao
        self.__view = SignUpFlyingMemberView(self)

    def openView(self):
        self.__view.show()
    
    def isEmpty(self, flyingMember):
        if flyingMember.cpf() != "" and flyingMember.name() != "" and flyingMember.phone() != "" and flyingMember.weight() != "" and flyingMember.height() != "":
            return True
        return False
    
    def signUp(self):
        isValid = self.isFormValid()
        if (not isValid):
            return
        
        newFlyingMember = FlyingMember(self.__view.cpfInput.text(), self.__view.nameInput.text(), self.__view.phoneInput.text(), self.__view.typeInput.currentText(), self.__view.weightInput.value(), self.__view.heightInput.value())
        self.__flyingMemberDAO.add(self.__view.cpfInput.text(), newFlyingMember)
        self.back()
        self.__view.clearInputs()
    
    def back(self):
        self.__view.close()
        self.__app.openFlyingMembersListView()

    def isFormValid(self):
        isValid = True
        self.__view.cpfError.setText("")
        self.__view.nameError.setText("")
        self.__view.phoneError.setText("")
        self.__view.weightError.setText("")
        self.__view.heightError.setText("")

        if(self.__view.cpfInput.text() == ""):
            self.__view.cpfError.setText("Insira seu CPF")
            isValid =  False
        
        if(self.__view.nameInput.text() == ""):
            self.__view.nameError.setText("Insira seu Nome")
            isValid =  False
        
        if(self.__view.phoneInput.text() == ""):
            self.__view.phoneError.setText("Insira seu número de telefone")
            isValid =  False
        
        if(self.__view.weightInput.value() == 0):
            self.__view.weightError.setText("Insira seu peso")
            isValid =  False
        
        if(self.__view.heightInput.value() == 0):
            self.__view.heightError.setText("Insira sua altura")
            isValid =  False
        
        
    
        members = self.__flyingMemberDAO.getAll()
        for member in members:
            if member.cpf == self.__view.cpfInput.text():
                self.__view.cpfError.setText("Existe um membro já cadastrado com este CPF!")
                isValid = False
                break
        return isValid
