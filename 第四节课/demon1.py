#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 20:42
# @Author  : lingxiangxiang
# @File    : demon1.py

def hello(name):
    print("hello {0}".format(name))

print("hell world")

for i in range(1, 100):
    print(i)



# if 条件判断
# 数据判断   （字符串）  1. 是否为空
# if a.strip():
# d      if type(a) == "dict"
d = dict(a=1)
if isinstance(d, dict):
    print("{0} is dict".format(d))

print(str(d) + "hello world")



m = [ x for x in range(1, 10)]
print(len(m))


# if 条件判断：
#   逻辑操作…………
#   ………


