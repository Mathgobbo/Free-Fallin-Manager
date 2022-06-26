from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QToolButton


class EditPlaneView(QMainWindow):
    
    def __init__(self, controller):
        super(EditPlaneView, self).__init__()
        self.__controller = controller
        uic.loadUi(r'.\src\resources\editPlane.ui', self)
        self.nameInput = self.findChild(QLineEdit, "name")
        self.nameError = self.findChild(QLabel, "nameError")
        self.modelInput = self.findChild(QLineEdit, "model")
        self.capacityInput = self.findChild(QLineEdit, "capacity")
        self.capacityInput.setInputMask("0009")
        self.emptyError = self.findChild(QLabel, "emptyError")

        self.saveButton = self.findChild(QPushButton, "saveButton")
        self.saveButton.clicked.connect(self.saveButtonClick)

        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.backButtonClick)
        
    # Chama o controlador e passa os valores dos campos de texto
    def saveButtonClick(self):
        self.nameError.setText("")
        self.emptyError.setText("")
        self.__controller.update(self.nameInput.text(), self.modelInput.text(), self.capacityInput.text())

    # Abre a tela
    def openEditPlaneView(self, plane):
        self.show()
        self.nameInput.setText(plane.name)
        self.modelInput.setText(plane.model)
        self.capacityInput.setText(plane.capacity_limit)

    # Retorna para a lista de aviões
    def backButtonClick(self):
        self.close()
        self.__controller.back()
        self.nameError.setText("")
        self.emptyError.setText("")

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