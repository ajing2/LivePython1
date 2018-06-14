#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 20:41
# @Author  : lingxiangxiang
# @File    : demon4.py
import requests

cookie = dict(_ga="GA1.2.208618761.1528809975", _gid="GA1.2.604525626.1528979734", PHPSESSID="ait0b8c22ofqpo630cekpc33b6", _gat="1", Hm_lvt_0936ebcc9fa24aa610a0079314fec2d3="1528809975,1528809984,1528979734,1528980228", Hm_lpvt_0936ebcc9fa24aa610a0079314fec2d3="1528980228", ape__Session="ait0b8c22ofqpo630cekpc33b6")


url = "http://httpbin.org/cookies"

session = requests.session()
res = session.get(url=url, cookies=cookie)
res.encoding = res.apparent_encoding
print(res.text)
