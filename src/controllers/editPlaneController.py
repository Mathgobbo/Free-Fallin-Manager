from src.models.Plane import Plane
from src.views.editPlaneView import EditPlaneView
from src.dao.planeDao import PlaneDao

class EditPlaneController:
    def __init__(self, app, planeDao) -> None:
        self.__view = EditPlaneView(self)
        self.__dao = planeDao
        self.__app = app
        self.__selectedPlane = None

    # Abre a view
    def openView(self, plane):
        self.__selectedPlane = plane
        self.__view.openEditPlaneView(plane)
    
    # Volta para lista de aviões
    def back(self):
        self.__view.close()
        self.__app.openPlaneList()

    # Atualiza o avião e persiste os dados
    def update(self, name, model, capacity_limit):
        if self.isEmpty(name, capacity_limit):
            if self.exist(name, model, capacity_limit):
                self.__view.invalidName()
            else:
                newPlane = Plane(name, model, capacity_limit)
                self.__dao.update(self.__selectedPlane.name, newPlane)
                self.back()
                self.__view.clearInputs()
        else:
            self.__view.emptyName()

    # Verifica se os campos obrigatórios estão vazios
    def isEmpty(self, name, capacity_limit):
        if name != "" and capacity_limit != "":
            return True
        return False

    # Verifica se já existem aviões com mesmo nome cadastrados
    def exist(self, name, model, capacity_limit): 
        planes = self.__dao.getAll()
        for plane in planes:
            if name == plane.name:
                return True
