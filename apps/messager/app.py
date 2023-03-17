from qtpy import QtWidgets
from design import messager


class MessagerApp(QtWidgets.QMainWindow, messager.Ui_Messager):

    """ Приложение мессенджера """

    def __init__(self):

        """ Функция инициализирует окно мессенджера """

        super().__init__()
        self.setupUi(self)
        self.sendMessageButton.clicked.connect(self.sendMessage)

    def sendMessage(self) -> None:
        """
        Функция отправляет сообщение введенное пользователем.
        :return: None
        """
        message = self.messageTextEdit.toPlainText()
