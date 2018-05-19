#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 21:27
# @Author  : lingxiangxiang
# @File    : demon3.py
import time

import multiprocessing


def add1(lock, value, number):
    with lock:
        print("start add1 number= {0}".format(number))
        for i in range(1, 5):
            number += value
            time.sleep(0.3)
            print("number = {0}".format(number))

def add3(lock, value, number):
    lock.acquire()
    print("start add3 number= {0}".format(number))
    try:
        for i in range(1, 5):
            number += value
            time.sleep(0.3)
            print("number = {0}".format(number))
    except Exception as e:
        raise e
    finally:
        lock.release()
        pass

if __name__ == '__main__':
    print("start main")
    number = 0
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=add1, args=(lock, 1, number))
    p3 = multiprocessing.Process(target=add3, args=(lock, 3, number))
    p1.start()
    p3.start()
    print("end main")
