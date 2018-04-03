#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 21:53
# @Author  : lingxiangxiang
# @File    : demon3.py

l1 = ["a", "b", "c", "d"]
l2 = [1, 2, 3, 4]
print(dict(zip(l1, l2)))

m = dict()
m.update({"a": 1})


print(type(m))
list()
int()
str()
float()
tuple()
dict()
# help(m.update())

print(isinstance(l1, list))
print(hasattr(l1, "append"))

# python2   raw_input   等于python3中的input    默认把输入作为字符串、
# python3  没有raw_input
#
# try:
#     name = raw_input("Please input your name:")
# except Exception as e:
#     name = input("Please input your name: ")
# finally:
#     print("hello {0}".format(name))


xx = [1, 2, 3, 4, 5, 6]
print(enumerate(xx))
for i,j in enumerate(xx):
    print(i,j)


print(str(tuple(dict(a=1, b=2))))