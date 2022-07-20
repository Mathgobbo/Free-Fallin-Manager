from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel


class PlaneRegistrationView(QMainWindow):
    
    def __init__(self, controller):
        self.__controller = controller
        super(PlaneRegistrationView, self).__init__()
        uic.loadUi(r'.\src\resources\planeRegistration.ui', self)

        self.nameInput = self.findChild(QLineEdit, "name")
        self.nameError = self.findChild(QLabel, "nameError")
     
        self.modelInput = self.findChild(QLineEdit, "model")

        self.capacityInput = self.findChild(QLineEdit, "capacity")
        self.capacityInput.setInputMask("99999999")
        self.emptyError = self.findChild(QLabel, "emptyError")

        self.registerButton = self.findChild(QPushButton, "registerButton")
        self.registerButton.clicked.connect(self.registerButtonClick)

        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)

    # Chama o controlador e passa os valores dos campos de texto
    def registerButtonClick(self):
        self.nameError.setText("")
        self.emptyError.setText("")
        self.__controller.register(self.nameInput.text(), self.modelInput.text(), self.capacityInput.text())

    # Abre a tela
    def openPlaneRegistrationView(self):
        self.show()
    
    # Retorna para a lista de aviões
    def backButtonClick(self):
        self.close()
        self.__controller.back()
        self.clearInputs()
    
    # Limpa os campos de texto
    def clearInputs(self):
        self.nameInput.setText("")
        self.modelInput.setText("")
        self.capacityInput.setText("")
        self.nameError.setText("")
        self.emptyError.setText("")

    # Atualiza mensagem de erro
    def emptyName(self):
        self.nameError.setText("Preencha os campos obrigatórios!")
        self.emptyError.setText("Preencha os campos obrigatórios!")

    # Atualiza mensagem de erro
    def invalidName(self):
        self.nameError.setText("Já existe um Avião registrado com este nome!")

  

