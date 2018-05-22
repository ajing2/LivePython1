#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 21:44
# @Author  : lingxiangxiang
# @File    : demon4.py
'''
多线程    密集型io
多线程的实现有两种方法：
方法1：
和多进程类似
方法2：
通过继承的方式
'''

import threading

def worker(args):
    print("开始子进程 {0}".format(args))
    print("结束子进程 {0}".format(args))

if __name__ == '__main__':

    print("start main")
    t1 = threading.Thread(target=worker, args=(1,))
    t2 = threading.Thread(target=worker, args=(2,))
    t1.start()
    t2.start()
    print("end main")
