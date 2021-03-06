# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class Params:

    def __init__(self):
        self.__dict__['src'] = ''
        self.__dict__['dst'] = ''

    def __getattr__(self, name):
        if name == 'src':
            return self.__dict__['src']
        if name == 'dst':
            return self.__dict__['dst']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'src':
            self.__dict__['src'] = value
        elif name == 'dst':
            self.__dict__['dst'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_SRC, self.__dict__['src'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DST, self.__dict__['dst'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['src'] = submsg.FindString(MSG_KEY_PARAMS_SRC)
        self.__dict__['dst'] = submsg.FindString(MSG_KEY_PARAMS_DST)