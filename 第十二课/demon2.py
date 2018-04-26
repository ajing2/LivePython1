#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 21:00
# @Author  : lingxiangxiang
# @File    : demon2.py

'''

'''
from io import StringIO, BytesIO

stringIO = StringIO()
stringIO.write("hello world")
stringIO.write("lalalalla, wo shi mai bao de xiao hang jia")
print(stringIO.getvalue())
stringIO.truncate(0)
print(stringIO.getvalue())






test = dict(a=1)
print(bytes(str(test).encode("utf-8")))