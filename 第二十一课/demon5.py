#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 20:38
# @Author  : lingxiangxiang
# @File    : demon5.py
from multiprocessing import Array, Process


def woker(arr):
    for i in range(len(arr)):
        arr[i] = -arr[i]

if __name__ == '__main__':
    arr = Array('i', [x for x in range(10)])
    print(arr)
    print(arr[:])
    p = Process(target=woker, args=(arr,))
    p.start()
    p.join()
    print(arr[:])