from src.views.reportView import ReportView

class ReportController:
    def __init__(self, app, flightDao) -> None:
        self.__app = app
        self.__dao = flightDao
        self.__view = ReportView(self)

    def openView(self):
        self.__view.show()

    def back(self):
        self.__app.openAdminMenu()
    
    def getFlights(self):
        return self.__dao.getAll()
