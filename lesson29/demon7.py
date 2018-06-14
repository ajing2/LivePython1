#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 21:28
# @Author  : lingxiangxiang
# @File    : demon7.py

'''

python3
data = urllib.parse.urlencode(data)
urllib.request.Request(url, data)

python2
data = urlib.urlencode(data)
urllib2.Request(url, data)

'''

import urllib
from urllib import parse
from urllib.request import Request


url = "http://www.baidu.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "Host": "www.baidu.com"
}
data = {"k1": "v1", "k2": "v2"}
data = parse.urlencode(data)
print(data)
response = Request(url=url, headers=headers, data=data)
print()
