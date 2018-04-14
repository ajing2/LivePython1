#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 22:00
# @Author  : lingxiangxiang
# @File    : demon5.py
import codecs


def px(item):
    pass
result = ""
with codecs.open("passwd", "r") as f:
    result = sorted(f.readlines(), key=lambda item: int(item.split(":")[2]))

with codecs.open("sortPasswd", "w") as f:
    f.writelines(result)