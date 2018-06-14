#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 21:11
# @Author  : lingxiangxiang
# @File    : demon6.py
'''
python2  urllib urllib2
python3  urllib

先来看一下python2
'''

import urllib, urllib2

url = "http://www.baidu.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "Host": "www.baidu.com"
}
data = {"k1": "v1", "k2": "v2"}
data = urllib.urlencode(data)
print(data)
response = urllib2.Request(url=url, headers=headers, data=data)
print()
