#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/23 20:12
# @Author  : lingxiangxiang
# @File    : demon1.py

import requests
from bs4 import BeautifulSoup



url = "http://www.apelearn.com/study_v2/chapter1.html"

session = requests.session()
res = session.get(url=url)
res.encoding = res.apparent_encoding
html_doc = res.text
# print(html_doc)
# print(type(html_doc))

soup = BeautifulSoup("<html>data</html>")
print(soup)
