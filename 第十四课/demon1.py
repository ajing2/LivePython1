#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 21:07
# @Author  : lingxiangxiang
# @File    : demon1.py
import re
import requests

url = "http://qwd.jd.com/fcgi-bin/qwd_searchitem_ex?skuid=26878432382%7C1658610413%7C26222795271%7C25168000024%7C11731514723%7C26348513019%7C20000220615%7C4813030%7C25965247088%7C5327182%7C19588651151%7C1780924%7C15495544751%7C10114188069%7C27036535156%7C10123099847%7C26016197600%7C10503200866%7C16675691362%7C15904713681"

session = requests.session()
r = session.get(url)
html = r.text
# print(html)

reg = re.compile(r"\"skuid\":\"(\d+)\",\s+\"\S+\s+\"skuurl\"\S+\s+\"skuimgurl\":\"(\S+)\",")
result = reg.findall(html)
print(result)


