#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 22:17
# @Author  : lingxiangxiang
# @File    : demon10.py
from urllib.request import Request, urlopen

url = "http://www.baidu.com"
req = Request(url)
res = urlopen(req)
print(res.read())