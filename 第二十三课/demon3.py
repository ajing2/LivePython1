#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 21:17
# @Author  : lingxiangxiang
# @File    : demon3.py
'''
Queue(maxsize=0)   指定队列大小，0表示无限
q.qsize()

'''
from Queue import Queue
q = Queue()
q.qsize()  #返回当前队列的空间
q.empty()  #判断当前队列是否为空
q.full()   #判断当前队列是否满
q.put()    #放消息
q.get()    #获取消息
q.task_done() #接受消息的线程调用该函数来说明消息对应的任务是否已经完成
q.join()    #等待队列为空，在执行别的操作