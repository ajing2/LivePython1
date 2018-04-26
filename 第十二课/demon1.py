#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 20:41
# @Author  : lingxiangxiang
# @File    : demon1.py

'''
加密  md5 rsa
hashlib

适用于python2'''
import hashlib
# m = hashlib.md5()
# src = "123456"
# m.update(src)
# print(m.hexdigest())

m3 = hashlib.md5("123456".encode("utf-8"))
src = bytes("ling", encoding="utf-8")
m3.update(src)
print(m3.hexdigest())
