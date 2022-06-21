from src.models.Plane import Plane
from src.views.planeRegistrationView import PlaneRegistrationView
from src.dao.planeDao import PlaneDao

class PlaneRegistrationController:
    def __init__(self, app, planeDao) -> None:
        self.__view = PlaneRegistrationView(self)
        self.__dao = planeDao
        self.__app = app

    def openView(self):
        self.__view.show()
    
    def back(self):
        self.__view.close()
        self.__app.openPlaneList()

    def register(self, name, model, capacity_limit):
        if self.isEmpty(name, capacity_limit):
            if self.exist(name, model, capacity_limit):
                self.__view.invalidName()
            else:
                newPlane = Plane(name, model, capacity_limit)
                self.__dao.add(name, newPlane)
                self.back()
                self.__view.clearInputs()
        else:
            self.__view.emptyName()

    # Verifica se os campos obrigatórios estão vazios
    def isEmpty(self, name, capacity_limit):
        if name != "" and capacity_limit != "":
            return True
        return False

    def exist(self, name, model, capacity_limit): 
        planes = self.__dao.getAll()
        for plane in planes:
            if name == plane.name:
                return False
