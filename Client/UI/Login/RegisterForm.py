# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QWidget

from .Ui_RegisterForm import Ui_Form


class Form(QWidget, Ui_Form):
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
