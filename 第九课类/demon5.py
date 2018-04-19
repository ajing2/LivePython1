#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 21:26
# @Author  : lingxiangxiang
# @File    : demon5.py

'''
host
port
username
password
dbname
'''

class DbArgs(object):
    # 只有类本身才可以调用
    __host = str("1.1.1.1")
    __port = str()
    __username = str()
    __password = str()
    __dbname = str()

    # 任何人可以调用
    name = "ajing"

    # 只能实例自己调用
    _host = "asdlfjasdl"
    def getHost(self):
        return self.__host

    def setHost(self, host):
        self.__host = host

dbArgs = DbArgs()
print(dbArgs.getHost())
dbArgs.name = "就是要改你，怎么的"
print(dbArgs.name)
print(dbArgs._host)
