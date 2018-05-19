#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 20:31
# @Author  : lingxiangxiang
# @File    : demon1.py

import multiprocessing

import time


def worker(args, interval):
    print("start worker {0}".format(args))
    time.sleep(interval)
    print("end worker {0}".format(args))

def main():
    print("start main")
    p1 = multiprocessing.Process(target=worker, args=(1, 1))
    p2 = multiprocessing.Process(target=worker, args=(2, 2))
    p3 = multiprocessing.Process(target=worker, args=(3, 3))
    p1.start()
    p1.join(timeout=0.5)
    p2.start()
    p3.start()
    print("the number of CPU is: {0}".format(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
       print("The name of active children is: {0}, pid is: {1} is alive".format(p.name, p.pid))
    print("end main")

if __name__ == '__main__':
    main()

