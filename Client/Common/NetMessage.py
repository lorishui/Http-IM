'''
Created on 2013年12月4日

@author: waterkit
'''
from Common.OpCode import *

class MsgList:
    def __init__(self):
        self.msgnum = 0
        self.msglist = []
       
    def addMsg(self,msg):
        if msg == None:
            return
        self.msglist.append(msg.toJsonDict());
        self.msgnum += 1
        
    def clear(self):
        del self.msglist[0:]
        self.msgnum = 0 
        
    def toJsonDict(self):
        jsonDict = {'msgnum':self.msgnum,'msglist':self.msglist}
        #print(jsonDict);
        return jsonDict
    
    def fromJsonDict(self,jsonDict):
        if 'msgnum' not in jsonDict.keys():
            return
        self.msgnum = jsonDict['msgnum']
        
        if 'msglist' not in jsonDict.keys():
            return
        self.msglist = jsonDict['msglist']
        

class NetMessage:
    def __init__(self,opcode):
        self.__opcode = opcode
        self.jsonDict = {}
        
    def setOpcode(self,opcode):
        self.__opcode = opcode;
    
    def getOpcode(self):
        return self.__opcode;
    
    def toJsonDict(self):
        self.jsonDict['opcode'] = self.__opcode
        return self.jsonDict
    
    def fromJsonDict(self,jsonDict):
        if 'opcode' not in jsonDict.keys():
            return
        self.setOpcode(jsonDict['opcode'])
        
class COPC_CS_TEST(NetMessage):
    def __init__(self,opcode = OPC_CS_TEST):
        NetMessage.__init__(self, opcode)
        self.testData = 0
        
    def toJsonDict(self):
        NetMessage.toJsonDict(self)
        self.jsonDict['testData'] = self.testData
        
        return self.jsonDict
    
    def fromJsonDict(self,jsonDict):
        NetMessage.fromJsonDict(self, jsonDict)
        self.testData = self.__jsonDict['testData']
        
class COPC_SC_TEST(NetMessage):
    def __init__(self,opcode = OPC_SC_TEST):
        NetMessage.__init__(self, opcode)
        self.name = ""
        
    def toJsonDict(self):
        NetMessage.toJsonDict(self)
        self.jsonDict['name'] = self.name
        return self.jsonDict
    
    def fromJsonDict(self,jsonDict):
        NetMessage.fromJsonDict(self, jsonDict)
        self.name = jsonDict['name']
    
