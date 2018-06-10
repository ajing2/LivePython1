#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 20:10
# @Author  : lingxiangxiang
# @File    : demon6.py

#
# urls = list()
#
# for i in range(1, 27):
#     url = 'http://www.apelearn.com/study_v2/chapter{0}.html'.format(i)
#     # print(url)
#     urls.append(url)
# # print(urls)
import re
import requests


reg = re.compile(r"<h3>目录列表</h3>\s+<ul>\s+([\s\S]*?</ul>)")
url = "http://www.apelearn.com/study_v2/"
session = requests.session()
r = session.get(url)
# print(r.encoding)
r.encoding = "utf-8"
html = r.text
# print(html)
htmlli = reg.findall(html)
# print(htmlli)
regurl = re.compile(r'''href="(.*?)"''')
if htmlli[0]:
    result = regurl.findall(htmlli[0])
    # print(result)

urls = list()
for i in result:
    url = "http://www.apelearn.com/study_v2/{0}".format(i)
    print(url)
    urls.append(urls)


