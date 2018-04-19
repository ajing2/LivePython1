#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 20:36
# @Author  : lingxiangxiang
# @File    : demon6.py

from random import randint

f = lambda n: 1 if n <=2 else f(n - 1) + f(n - 2)
def f(n):
    if n<=2:
        return 1
    else:
        return f(n-1)+ f(n-2)

a = b = [1, 10]
a = [1, 1000]
b = [1, 1000]
a.append(f(randint(a[0], a[1])))
print(a, end="")
b.append(f(randint(b[0], b[1])))
print(b)

# 1, 1, 2, 3, 5, 8
# [1, 1000, 8][1, 1000, 8, 13]

# randint(a[0], a[1])
# randint(1, 1000)