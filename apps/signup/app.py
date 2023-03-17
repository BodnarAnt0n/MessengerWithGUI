from qtpy import QtWidgets
from design import signup


class SignUpApp(QtWidgets.QMainWindow, signup.Ui_SignUp):

    """ Приложение для регистрации пользователя """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
