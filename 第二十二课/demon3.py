#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 21:12
# @Author  : lingxiangxiang
# @File    : demon3.py
import time

import multiprocessing


def fun(msg):
    print("#########start#### {0}".format(msg))
    time.sleep(3)
    print("#########end###### {0}".format(msg))


if __name__ == '__main__':
    print("start main")
    pool = multiprocessing.Pool(processes=3)
    for i in range(1, 7):
        msg = "hello {0}".format(i)
        pool.apply_async(fun, (msg,))# 执行时间6s+
        # pool.apply(fun, (msg,))   6*3=18+#执行时间
    pool.close()#在调用join之前，要先调用close，否则会报错，close执行完不会有新的进程加入到pool
    pool.join()#join 是等待所有的子进程结束
    print("end main")

# pool.apply_async   非阻塞，定义的进程池最大数的同时执行
# pool.apply    一个进程结束，释放回进程池，开始下一个进程
