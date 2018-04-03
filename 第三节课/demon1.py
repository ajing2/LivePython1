#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 20:11
# @Author  : lingxiangxiang
# @File    : demon1.py
import os



print(os.listdir('.'))
a = "asdfas"
print(a.find("a"))
print(a.find("m"))

student = ["lingxiangxiang", "molin", "chengli"]
a = ["1", "2", "3", "4"]


# []   list
# ()   tuple
# {}   dict


x = dict()
y = dict(a=1)
z = {"name": "ling"}
m = dict([("name", "ling"), ("age", 18)])
n = m.copy()
print(m)

print(m.get("name11"))
# print(m.pop("name"))


print(n)
# m.clear()
print(m.keys())
print(m.values())
print(m.items())

for i in m.items():
    print(i[0])
    print(i[1])

a, b = ("1", "2")
print(a)
print(b)

# update 相当于  +






# print("---".join(a))
