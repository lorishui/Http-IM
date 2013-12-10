# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/Git/Http-IM/Client/UI/Login/LoginForm.ui'
#
# Created: Tue Dec 10 22:35:39 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_login_form(object):
    def setupUi(self, login_form):
        login_form.setObjectName(_fromUtf8("login_form"))
        login_form.resize(449, 248)
        login_form.setMinimumSize(QtCore.QSize(449, 248))
        login_form.setMaximumSize(QtCore.QSize(449, 248))
        self.label = QtGui.QLabel(login_form)
        self.label.setGeometry(QtCore.QRect(150, 60, 31, 21))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_loginID = QtGui.QLineEdit(login_form)
        self.lineEdit_loginID.setGeometry(QtCore.QRect(190, 60, 121, 27))
        self.lineEdit_loginID.setObjectName(_fromUtf8("lineEdit_loginID"))
        self.lineEdit_loginPassWD = QtGui.QLineEdit(login_form)
        self.lineEdit_loginPassWD.setGeometry(QtCore.QRect(190, 100, 121, 27))
        self.lineEdit_loginPassWD.setObjectName(_fromUtf8("lineEdit_loginPassWD"))
        self.label_2 = QtGui.QLabel(login_form)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 71, 21))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Button_askRegister = QtGui.QPushButton(login_form)
        self.Button_askRegister.setGeometry(QtCore.QRect(320, 60, 98, 27))
        self.Button_askRegister.setObjectName(_fromUtf8("Button_askRegister"))
        self.Button_askPassWD = QtGui.QPushButton(login_form)
        self.Button_askPassWD.setGeometry(QtCore.QRect(320, 100, 98, 27))
        self.Button_askPassWD.setObjectName(_fromUtf8("Button_askPassWD"))
        self.checkBox = QtGui.QCheckBox(login_form)
        self.checkBox.setGeometry(QtCore.QRect(130, 140, 97, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(login_form)
        self.checkBox_2.setGeometry(QtCore.QRect(250, 140, 97, 22))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.Button_login = QtGui.QPushButton(login_form)
        self.Button_login.setGeometry(QtCore.QRect(120, 200, 211, 31))
        self.Button_login.setObjectName(_fromUtf8("Button_login"))
        self.line = QtGui.QFrame(login_form)
        self.line.setGeometry(QtCore.QRect(0, 180, 451, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_3 = QtGui.QLabel(login_form)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 101, 81))
        self.label_3.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));"))
        self.label_3.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_3.setFrameShadow(QtGui.QFrame.Plain)
        self.label_3.setMidLineWidth(0)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(login_form)
        QtCore.QMetaObject.connectSlotsByName(login_form)

    def retranslateUi(self, login_form):
        login_form.setWindowTitle(QtGui.QApplication.translate("login_form", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("login_form", "ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("login_form", "PassWD:", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_askRegister.setText(QtGui.QApplication.translate("login_form", "注册帐号", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_askPassWD.setText(QtGui.QApplication.translate("login_form", "忘记密码", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("login_form", "记住密码", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("login_form", "自动登录", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_login.setText(QtGui.QApplication.translate("login_form", "登录", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    login_form = QtGui.QWidget()
    ui = Ui_login_form()
    ui.setupUi(login_form)
    login_form.show()
    sys.exit(app.exec_())

