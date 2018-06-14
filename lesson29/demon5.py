#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 20:59
# @Author  : lingxiangxiang
# @File    : demon5.py

import requests

url = "http://2018.ip138.com/ic.asp"

proxy = {"http": "http://221.228.17.172:8181"}

res1 = requests.get(url=url, proxies=proxy)
res2 = requests.get(url=url)
res1.encoding = res1.apparent_encoding
res2.encoding = res2.apparent_encoding

print(res1.text)
print("###"*10)
print(res2.text)


