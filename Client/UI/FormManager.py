'''
Created on 2013年12月10日

@author: water
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Common.XmlTools import *
from UI.Login.LoginForm import  *
from UI.Login.RegisterForm import *

(
    LOGIN_FORM,
    REGISTER_FORM,
    
) = range(2)

class FormManager(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.url = ""
        self.curFormIndex = LOGIN_FORM
        self.loginForm = LoginForm()
        
    def readConfig(self):
        doc = minidom.parse('Config.xml')
        root = doc.documentElement

        ip_node = get_xmlnode(root,'ip')
        self.__ip = get_nodevalue(ip_node[0])
        
    def start(self):
        self.loginForm.show()
        pass
        