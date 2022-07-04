from src.dao.flyingMemberDao import FlyingMemberDAO
from src.models.FlyingMember import FlyingMember
from src.views.editMemberView import EditMemberView


class EditMemberController:
    def __init__(self, app, flyMemberDao) -> None:
        self.__view = EditMemberView(self)
        self.__dao = flyMemberDao
        self.__app = app
        self.__selectedMember = None
    
    def openView(self, member):
        self.__selectedMember = member
        self.__view.openEditMemberView(member)
    
    def back(self):
        self.__view.close()
        self.__app.openFlyingMembersListView()
    
    def save(self):
        isValid = self.isFormValid()
        if (not isValid):
            return
        
        newMember = FlyingMember(self.__view.cpfInput.text(), self.__view.nameInput.text(), self.__view.phoneInput.text(), self.__view.typeInput.currentText(), self.__view.weightInput.value(), self.__view.heightInput.value())
        self.__dao.update(self.__selectedMember.cpf, newMember)
        self.back()
        self.__view.clearInputs()
    
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
        
        return isValid
        
        # members = self.__dao.getAll()
        # for member in members:
        #    if member.cpf == self.__view.cpfInput.text():
        #        self.__view.cpfError.setText("Existe um membro já cadastrado com este CPF!")
        #        isValid = False
        #        break
        # return isValid