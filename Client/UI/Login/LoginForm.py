# -*- coding: utf-8 -*-

"""
Module implementing LoginForm.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from UI.Login.Ui_LoginForm import Ui_login_form


class LoginForm(QWidget, Ui_login_form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_Button_askRegister(self):
        pass