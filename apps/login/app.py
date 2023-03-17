from qtpy import QtWidgets
from design import login
from apps.signup.app import SignUpApp
from apps.messager.app import MessagerApp


class LoginApp(QtWidgets.QMainWindow, login.Ui_Login):

    """ Приложение для авторизации пользователя """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Подключение дочерних окон
        self.login_window = MessagerApp()
        self.signUpWindow = SignUpApp()

        # Подключение событий к кнопкам
        self.loginButton.clicked.connect(self.loginEvent)
        self.signUpButton.clicked.connect(self.signUpEvent)

    def loginEvent(self):

        """ Событие по авторизации и переходу в приложение мессенджера """

        login = self.loginInput.text()
        password = self.passwordInput.text()

        # TODO: Авторизация

        # TODO: Сохранить пользователя в текущую сессию

        # Закрытие окна авторизации и открытие окна мессенджера

        self.login_window.show()
        self.close()

    def signUpEvent(self):

        """ Событие по переходу в приложение регистрации """

        self.signUpWindow.show()
        self.close()

