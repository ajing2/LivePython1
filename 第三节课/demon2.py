#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 21:35
# @Author  : lingxiangxiang
# @File    : demon2.py
# update 相当于+

m = dict()

a = dict(a=1, b=2)
b = dict(x=10, y=20)
a.update(b)
print(a)

m.update(a)
print(a)


# print(a.items())
# print(a.iteritems())
# for i in a.iteritems():
#     print(i)
print(type(a.items()))
y = dict()
x = ["1", "2", "3", "4", "5"]
yy = y.fromkeys(x, "hello")
print(yy)

