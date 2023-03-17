import sys
from qtpy import QtWidgets
from apps.login.app import LoginApp


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
