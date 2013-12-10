'''
Created on 2013年12月4日

@author: waterkit
'''

from Common.LogicCenter import *

# l = LogicCenter()
# opc = COPC_CS_TEST()
# opc.testData = 999
# l.addSendMsg(opc)
# l.sendMsg()
# l.procMsg()

import sys
from PyQt4 import QtGui
#from UI.Login.LoginForm import *
from UI.FormManager import *


app = QtGui.QApplication(sys.argv)
#qb = LoginForm()
#qb.show()
fm = FormManager()
fm.start()
app.exec_()