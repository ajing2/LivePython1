#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 20:35
# @Author  : lingxiangxiang
# @File    : demon3.py

import requests

url = "http://www.hao123.com/"

session = requests.session()
response  = session.get(url=url).text
cookies = session.cookies
print(cookies.keys())
print(cookies.values())

for cookie in cookies:
    print(cookie.name)
    print(cookie.value)
    print(cookie.domain)
    print(cookie.path)
    print(cookie.expires)
