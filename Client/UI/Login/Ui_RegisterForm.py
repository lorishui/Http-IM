# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/Git/HttpQQ/Client/UI/Login/RegisterForm.ui'
#
# Created: Tue Dec 10 20:34:46 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(316, 266)
        self.register_frame = QtGui.QFrame(Form)
        self.register_frame.setGeometry(QtCore.QRect(10, 10, 291, 251))
        self.register_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.register_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.register_frame.setObjectName(_fromUtf8("register_frame"))
        self.lineEdit_3 = QtGui.QLineEdit(self.register_frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 90, 113, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_2 = QtGui.QLabel(self.register_frame)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 61, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.register_frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(self.register_frame)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 61, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.register_frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 50, 113, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(self.register_frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 61, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(self.register_frame)
        self.label_4.setGeometry(QtCore.QRect(30, 130, 61, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_4 = QtGui.QLineEdit(self.register_frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 130, 171, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pushButton = QtGui.QPushButton(self.register_frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 190, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "PassWD:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "PassWD:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "EMail:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Register", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

