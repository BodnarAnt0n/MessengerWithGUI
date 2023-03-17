# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design\messager.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Messager(object):
    def setupUi(self, Messager):
        Messager.setObjectName("Messager")
        Messager.setEnabled(True)
        Messager.resize(419, 600)
        Messager.setStyleSheet("QWidget{\n"
"    background-color: rgb(255, 255, 255)\n"
"}")
        self.messageTextEdit = QtWidgets.QTextEdit(Messager)
        self.messageTextEdit.setGeometry(QtCore.QRect(10, 530, 271, 31))
        self.messageTextEdit.setStyleSheet("#messageTextEdit{\n"
"    padding: 6px 12px;\n"
"    font-size: 16px;\n"
"    font-weight: 400;\n"
"    line-height: 1.5;\n"
"    color: #212529;\n"
"    background-color: #fff;\n"
"    background-clip: padding-box;\n"
"    border: 1px solid #ced4da;\n"
"    appearance: none;\n"
"    border-radius: 4px;\n"
"    transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;\n"
"}\n"
"#messageTextEdit:focus{\n"
"    color: #212529;\n"
"    background-color: #fff;\n"
"    border-color: #86b7fe;\n"
"    outline: 0;\n"
"    box-shadow: 0 0 0 0.25rem rgb(13 110 253 / 25%);\n"
"}\n"
"                ")
        self.messageTextEdit.setObjectName("messageTextEdit")
        self.sendMessageButton = QtWidgets.QPushButton(Messager)
        self.sendMessageButton.setGeometry(QtCore.QRect(290, 530, 111, 31))
        self.sendMessageButton.setStyleSheet("/* CSS */\n"
"#sendMessageButton {\n"
"  background-color: #FFFFFF;\n"
"  border: 1px solid rgb(209,213,219);\n"
"  border-radius: .5rem;\n"
"  box-sizing: border-box;\n"
"  color: #111827;\n"
"  font-family: \"Inter var\",ui-sans-serif,system-ui,-apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Arial,\"Noto Sans\",sans-serif,\"Apple Color Emoji\",\"Segoe UI Emoji\",\"Segoe UI Symbol\",\"Noto Color Emoji\";\n"
"  font-size: .875rem;\n"
"  font-weight: 600;\n"
"  line-height: 1.25rem;\n"
"  padding: .75rem 1rem;\n"
"  text-align: center;\n"
"  text-decoration: none #D1D5DB solid;\n"
"  text-decoration-thickness: auto;\n"
"  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"#sendMessageButton:hover {\n"
"  background-color: rgb(249,250,251);\n"
"}\n"
"\n"
"#sendMessageButton:focus {\n"
"  outline: 2px solid transparent;\n"
"  outline-offset: 2px;\n"
"}\n"
"\n"
"#sendMessageButton:focus-visible {\n"
"  box-shadow: none;\n"
"}")
        self.sendMessageButton.setCheckable(False)
        self.sendMessageButton.setObjectName("sendMessageButton")

        self.retranslateUi(Messager)
        QtCore.QMetaObject.connectSlotsByName(Messager)

    def retranslateUi(self, Messager):
        _translate = QtCore.QCoreApplication.translate
        Messager.setWindowTitle(_translate("Messager", "Мессенджер"))
        self.messageTextEdit.setHtml(_translate("Messager", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">Введите сообщение:</span></p></body></html>"))
        self.sendMessageButton.setText(_translate("Messager", "Отправить"))
