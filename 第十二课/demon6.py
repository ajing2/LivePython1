#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 22:25
# @Author  : lingxiangxiang
# @File    : demon6.py
import codecs
import json

test = {"a": 1, "b": 2}
with codecs.open("1.txt", "w") as f:
    json.dump(test, f)

with codecs.open("1.txt", "r") as f:
    aa = json.load(f)
    print(aa)
    print(type(aa))