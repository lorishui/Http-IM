# -*- coding: utf-8 -*-

"""
Module implementing LoginForm.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from UI.Login.Ui_LoginForm import Ui_login_form
#from UI.Login.RegisterForm import *
from UI.Login.Register_DL import *
from UI.Login.AskPassWD_DL import *


class LoginForm(QWidget, Ui_login_form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.register_DL = Dialog_register(self)
        self.askPassWD_DL = Dialog_askPassWD(self)
        
    @pyqtSlot()
    def on_Button_askRegister_clicked(self):
        self.register_DL.show()
        
    @pyqtSlot()
    def on_Button_askPassWD_clicked(self):
        self.askPassWD_DL.show()
        
        
        