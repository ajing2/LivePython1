#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 21:55
# @Author  : lingxiangxiang
# @File    : demon8.py
import codecs

import requests
url = "https://img.alicdn.com/tfs/TB1MjYowCBYBeNjy0FeXXbnmFXa-520-280.jpg_q90_.webp"
res = requests.get(url=url, stream=True)

with codecs.open("hz.jpg", "wb") as f:
    for chunk in res.iter_content(10000):
        f.write(chunk)



