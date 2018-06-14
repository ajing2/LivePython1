#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 20:58
# @Author  : lingxiangxiang
# @File    : demon1.py


import requests

wd = "python"
params = {"wd": "hello"}
url = "http://www.baidu.com/s"
r = requests.post(url=url, data=params)
requests.post()
r.encoding = "utf-8"
print(r.url)
html = r.text
# print(html)