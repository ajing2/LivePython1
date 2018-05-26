#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 20:36
# @Author  : lingxiangxiang
# @File    : demon1.py
'''
一个是生产者
一个是消费者
创建一个队列    q = Queue()
发消息：   q.put()
收消息：   data = q.get()
'''
from multiprocessing import Queue, Pipe
from threading import Thread

import time


def produce(q):
    print("start produce")
    for i in range(10):
        q.put(i)
        print("produce has produced value {0}".format(i))
        time.sleep(0.3)
    print("end produce")

def custome(q):
    print("start custorme")
    while 1:
        data = q.get()
        print("custormer has get value {0}".format(data))



if __name__ == '__main__':
    q = Queue()
    p = Thread(target=produce, args=(q,))
    c = Thread(target=custome, args=(q, ))
    p.start()
    c.start()
#     Pipe
