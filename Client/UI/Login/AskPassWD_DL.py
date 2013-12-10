# -*- coding: utf-8 -*-

"""
Module implementing Dialog_askPassWD.
"""

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog

from .Ui_AskPassWD_DL import Ui_Dialog_askPassWD


class Dialog_askPassWD(QDialog, Ui_Dialog_askPassWD):
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
