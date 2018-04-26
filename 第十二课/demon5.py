#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 22:16
# @Author  : lingxiangxiang
# @File    : demon5.py

'''python2 才有一下的情况'''
import json
a = dict(hello="你好")
print(a)
print(a["hello"])
print(str(a))
print(json.dumps(a, ensure_ascii=False))

