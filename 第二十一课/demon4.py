#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 21:27
# @Author  : lingxiangxiang
# @File    : demon3.py
import time

import multiprocessing

from multiprocessing import Value, Array, Manager


def add1(value, number):
    print("start add1 number= {0}".format(number.value))
    for i in range(1, 5):
        number.value += value
        print("number = {0}".format(number.value))

def add3(value, number):
    print("start add3 number= {0}".format(number.value))
    try:
        for i in range(1, 5):
            number.value += value
            print("number = {0}".format(number.value))
    except Exception as e:
        raise e

if __name__ == '__main__':
    print("start main")
    number = Value('d', 0)
    p1 = multiprocessing.Process(target=add1, args=(1, number))
    p3 = multiprocessing.Process(target=add3, args=(3, number))
    p1.start()
    p3.start()
    print("end main")

