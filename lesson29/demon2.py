#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 21:53
# @Author  : lingxiangxiang
# @File    : demon2.py
'''
session = requests.session()
session.get()
session.post()

'''
import requests
# session = requests.session()
# session.post()
# session.get()


url = "https://www.qiushibaike.com/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}



r = requests.get(url=url, headers=header)
print(r.request)
print(r.headers)
print(r.headers.get("User-Agent"))
print(r.encoding)
# print(r.text)
r.encoding = r.apparent_encoding
print(r.cookies)
print(r.cookies.get("_xsrf"))
print(r.url)
print(r.status_code)
#r.text
#r.encoding