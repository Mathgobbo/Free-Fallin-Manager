from src.views.planeListView import PlaneListView

class PlaneListController:
    def __init__(self, app, planeDao) -> None:
        self.__app = app
        self.__dao = planeDao
        self.__view = PlaneListView(self)

    def openView(self):
        self.__view.show()

    def back(self):
        self.__app.openAdminMenu()

    def goToPlaneRegistration(self):
        self.__view.close()
        self.__app.openPlaneRegistration()
    
    def getPlanes(self):
        return self.__dao.getAll()

    def deletePlane(self, name):
        self.__dao.remove(name)
    
    def editPlane(self, plane):
        self.__view.close()
        self.__app.openEditPlane(plane)
