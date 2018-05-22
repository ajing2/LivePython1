#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 20:44
# @Author  : lingxiangxiang
# @File    : demon1.py

'''
强大Manage
'''
from multiprocessing import Manager, Process


def worker(dt, lt):
    for i in range(10):
        dt[i] = i*i

    lt += [x for x in range(11, 16)]




if __name__ == '__main__':
    manager = Manager()
    dt = manager.dict()
    lt = manager.list()
    p = Process(target=worker, args=(dt, lt))
    p.start()
    p.join(timeout=3)
    print(dt)
    print(lt)