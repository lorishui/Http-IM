# -*- coding: utf-8 -*-

"""
Module implementing Dialog_register.
"""

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog

from .Ui_Register_DL import Ui_Dialog_register


class Dialog_register(QDialog, Ui_Dialog_register):
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
