#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 22:08
# @Author  : lingxiangxiang
# @File    : demon2.py
import codecs
import re

import os

regUpstream = re.compile(r"\s*(upstream\s+(\S+)\s+{[^}]+})")

with codecs.open("ga10.wms5.jd.com.txt") as fu:
    textList = regUpstream.findall(fu.read())
    if not os.path.exists("upstream"):
        os.mkdir("upstream")
    os.chdir("upstream")
    for item in textList:
        with codecs.open(item[1], "w") as fw:
            fw.write(item[0])
    os.chdir("..")



regLocation = re.compile(r"(location\s+/(\S+)/\s+{\s+proxy_next_upstream.*[^]]*?})")
with codecs.open("ga10.wms5.jd.com.txt") as fl:
    textLocation = regLocation.findall(fl.read())
    if not os.path.exists("location"):
        os.mkdir("location")
    os.chdir("location")
    for each in textLocation:
        file = each[1] + ".locaion.conf"
        with codecs.open(file, "w") as flw:
            flw.write(each[0])