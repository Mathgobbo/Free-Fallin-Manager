from src.models.Fly import Fly
from src.views.flightRegistrationView import FlightRegistrationView


class FlightRegistrationController:

    def __init__(self, app) -> None:
        self.__app = app
        self.__view = FlightRegistrationView(self)

    def openView(self):
        self.__view.show()

    def goToAddMember(self):
        self.__app.openAddMemberView()
