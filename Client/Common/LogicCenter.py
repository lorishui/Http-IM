'''
Created on 2013年12月4日

@author: waterkit
'''
import json,urllib.request
import threading
from Common.NetMessage import *

class LogicCenter:
    def __init__(self):
        self.serverUrl = "http://localhost/QQ_Http/index.php"
        self.timeout = 0
        self.__lock = threading.Lock()
        self.sendMsgList = MsgList()
        self.recvMsgList = []
        
    def addSendMsg(self,msg):
        if msg == None:
            return
        self.sendMsgList.addMsg(msg)
        
    def sendMsg(self):
        if self.sendMsgList.msgnum <= 0:
            return
        
        values = {}
        values['info'] = json.dumps(self.sendMsgList.toJsonDict())
        url_values = urllib.parse.urlencode(values)
        url_values = url_values.encode('utf-8')
        
        returnInfo = urllib.request.urlopen("http://localhost/QQ_Http/index.php", url_values)
        returnInfo = returnInfo.read().decode('utf-8')
        print(returnInfo)
        info = json.loads(returnInfo)
        self.recvMsg(info)

#         info = urllib.request.urlopen("http://localhost/QQ_Http/index.php")
#         info = info.read().decode('utf-8')
#         print(info)
        
    def recvMsg(self,info):
        self.__lock.acquire()
        opc = MsgList()
        opc.fromJsonDict(info)
        self.recvMsgList += opc.msglist;
        self.__lock.release()
        
    def getRecvMsg(self):
        self.__lock.acquire()
        if len(self.recvMsgList) <= 0:
            self.__lock.release()
            return None
        wp = self.recvMsgList[0]
        del self.recvMsgList[0]
        self.__lock.release()
        return wp
    
    def procMsg(self):
        while True:
            netdata = self.getRecvMsg()
            if netdata == None:
                break
            self._procMsg(netdata)
            
            
    def _procMsg(self,netdata):
        netdata = json.loads(netdata);
        if 'opcode' not in netdata.keys():
            return
        
        opcode = netdata['opcode']
        
        if opcode == OPC_SC_TEST:
            opc = COPC_SC_TEST()
            opc.fromJsonDict(netdata)
            print(opc.name)
        
        