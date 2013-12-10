# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/Git/Http-IM/Client/UI/Login/Register_DL.ui'
#
# Created: Tue Dec 10 22:44:48 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog_register(object):
    def setupUi(self, Dialog_register):
        Dialog_register.setObjectName(_fromUtf8("Dialog_register"))
        Dialog_register.setWindowModality(QtCore.Qt.WindowModal)
        Dialog_register.resize(313, 239)
        self.pushButton = QtGui.QPushButton(Dialog_register)
        self.pushButton.setGeometry(QtCore.QRect(50, 200, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog_register)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 100, 113, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog_register)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 140, 171, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_2 = QtGui.QLabel(Dialog_register)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 61, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Dialog_register)
        self.label_4.setGeometry(QtCore.QRect(40, 140, 61, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label = QtGui.QLabel(Dialog_register)
        self.label.setGeometry(QtCore.QRect(30, 20, 61, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Dialog_register)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 61, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog_register)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 60, 113, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit = QtGui.QLineEdit(Dialog_register)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_2 = QtGui.QPushButton(Dialog_register)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 200, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog_register)
        QtCore.QMetaObject.connectSlotsByName(Dialog_register)

    def retranslateUi(self, Dialog_register):
        Dialog_register.setWindowTitle(QtGui.QApplication.translate("Dialog_register", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog_register", "Register", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_register", "PassWD:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog_register", "EMail:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_register", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_register", "PassWD:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog_register", "Return", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_register = QtGui.QDialog()
    ui = Ui_Dialog_register()
    ui.setupUi(Dialog_register)
    Dialog_register.show()
    sys.exit(app.exec_())

