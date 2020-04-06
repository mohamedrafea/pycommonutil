# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:48:57 2017

@author: mohamed
"""
from pycommonutil import list_util
import json
class Common(object):
    excludedFields = {}
    def toJSON(self, excludedFields={}):
        d = self.__dict__
        for k in sorted(self.__dict__.keys()):
            if k[0] == '_' or k in excludedFields:
                d.pop(k, None)
        return json.dumps(d)

    def __repr__(self):
        return "<{}({})>".format(
            self.__class__.__name__,
            ', '.join(
                ["{}={}".format(k, repr(self.__dict__[k]))
                    for k in sorted(self.__dict__.keys())
                    if k[0] != '_' and k not in self.excludedFields]
            )
        )
    """
    def copy(self,orig,excludedFields={}):
        for k in sorted(orig.__dict__.keys()):
            if k[0] != '_' and k not in excludedFields:
                self.__dict__[k] = orig.__dict__[k]
    """
    def copy(self, orig):
        for k in sorted(orig.__dict__.keys()):
            if k[0] != '_':
                self.__dict__[k] = orig.__dict__[k]

    @classmethod
    def toCSV(self,objects,fileName,separator=','):
        out = open(fileName, 'w')
        out.write(objects[0].rowHeader(separator))
        for o in objects:
            out.write(o.rowValues(separator))
        out.close()
    def rowHeader(self,separator=','):
        h = ''
        for k in sorted(self.__dict__.keys()):
            if k[0] != '_':
                if len(h)==0:
                    h = k
                else:
                    h = h + separator+k
        return h+'\n'

    def rowValues(self,separator=','):
        r = None
        for k in sorted(self.__dict__.keys()):
            if k[0] != '_':
                v = ''
                rv = self.__dict__[k]
                if rv is not None:
                    if type(rv) is list:
                        v = list_util.convertListToPostGresList(rv)
                    else:
                        v = str(rv)
                if k=='areas':
                    print(v)
                    print(type(rv))
                    #print(k)
                    #print(type(self.__dict__[k]))
                if r is None:
                    r = v
                else:
                    r = r + separator+v
        return r+'\n'


