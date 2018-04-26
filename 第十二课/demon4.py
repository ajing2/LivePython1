#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 22:04
# @Author  : lingxiangxiang
# @File    : demon4.py
import json

import requests

url = "http://qwd.jd.com/fcgi-bin/qwd_activity_list?g_tk=1231472791&env=3"
session = requests.session()
r = session.get(url)
result = json.loads(r.text)
print(result["errCode"])
print(result["msg"])

