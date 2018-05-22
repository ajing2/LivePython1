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

import time


class Hello(threading.Thread):
    def __init__(self, args):
        super(Hello, self).__init__()
        self.args = args
        global a
        print("a = {0}".format(a))
        a += 1

    def run(self):
        print("开始子进程 {0}".format(self.args))
        print("结束子进程 {0}".format(self.args))

if __name__ == '__main__':
    a = 1
    print("start main")
    t1 = Hello(5)
    time.sleep(3)
    t2 = Hello(5)
    t1.start()
    t2.start()
    print("#####a = {0}####".format(a))
    print("end main")

