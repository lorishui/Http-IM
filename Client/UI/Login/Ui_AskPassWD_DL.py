# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/Git/Http-IM/Client/UI/Login/AskPassWD_DL.ui'
#
# Created: Tue Dec 10 22:39:12 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog_askPassWD(object):
    def setupUi(self, Dialog_askPassWD):
        Dialog_askPassWD.setObjectName(_fromUtf8("Dialog_askPassWD"))
        Dialog_askPassWD.setWindowModality(QtCore.Qt.WindowModal)
        Dialog_askPassWD.resize(323, 153)
        self.lineEdit = QtGui.QLineEdit(Dialog_askPassWD)
        self.lineEdit.setGeometry(QtCore.QRect(100, 40, 181, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog_askPassWD)
        self.label.setGeometry(QtCore.QRect(30, 40, 66, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog_askPassWD)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog_askPassWD)
        QtCore.QMetaObject.connectSlotsByName(Dialog_askPassWD)

    def retranslateUi(self, Dialog_askPassWD):
        Dialog_askPassWD.setWindowTitle(QtGui.QApplication.translate("Dialog_askPassWD", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_askPassWD", "Email:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog_askPassWD", "Send", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_askPassWD = QtGui.QDialog()
    ui = Ui_Dialog_askPassWD()
    ui.setupUi(Dialog_askPassWD)
    Dialog_askPassWD.show()
    sys.exit(app.exec_())

