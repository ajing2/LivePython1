#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 20:59
# @Author  : lingxiangxiang
# @File    : demon2.py
def worker(dt, lt):
    for i in range(10):
        key = "args" + str(i)
        dt[key] = i*i
    print(dt)

    lt += [x for x in range(10)]
    print(lt)


worker(dict(), list())