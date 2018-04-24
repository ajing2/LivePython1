#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 21:23
# @Author  : lingxiangxiang
# @File    : demon3.py
from datetime import datetime, timedelta

print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)
print(datetime.now().microsecond)
print(datetime.now().strftime("%Y-%m-%d"))
print(type(datetime.now().strftime("%Y-%m-%d")))
# str from time
print(type(datetime.now()))

a = datetime.now().strptime("2018-04-22", "%Y-%m-%d")
print(type(a))
# 2018-04-22.nginx.log

nowTime = datetime.now()
nowTime += timedelta(hours=+3)
print(nowTime)




import time
# time.sleep(10)
print(time.time())
# 时间戳就是通1970-01-01 开始，到现在的秒数

print(time.ctime())
print(time.localtime())