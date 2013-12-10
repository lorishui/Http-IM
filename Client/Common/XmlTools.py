'''
Created on 2013年9月5日

@author: Administrator
'''
from xml.dom import minidom

def get_attrvalue(node, attrname):
    return node.getAttribute(attrname) if node else ''

def get_nodevalue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''

def set_nodevalue(node, value,index = 0):
    if node:
        node.childNodes[index].nodeValue = value

def get_xmlnode(node,name):
    return node.getElementsByTagName(name) if node else []

def save_xml(doc,filename):
    f = open(filename,'w')
    import codecs
    writer = codecs.lookup('utf-8')[3](f)
    doc.writexml(f)
    writer.close()
