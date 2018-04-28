#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 20:32
# @Author  : lingxiangxiang
# @File    : demon7.py
import codecs

with codecs.open("1.txt", "r") as f:
    pass
m = dict(b=2, a=1)
print(m)
print(dict(sorted(m.items(), key=lambda d:d[1])))

a = lambda x: x*x
print([x for x in range(1, 10) if x%2==0])
# ()  []
# return yield

# 组  test1 test2  test3   id   组名
# 人  aaa   bbb    ccc     id    人名
# 人组关系表 aaa  test1    bbb  test3  aaa test3  id  组id   人id


# 组    组员


# select   人   关系  关联   组id


# select * from b, c where b.id = c.人id          y  50
# select  组名  组id    x  10
# 10*50
#
# for i in x:
#     for j in y:
#         if x.id == y.组id
#            符合条件了
#
# mmm = dict()
# for j in y:
#     mmm[组id] = 组员名字
#
#
# result = dict()#  key  组名    value  list()
# for i in x:
#     value = mmm.get(i.组id)
#     if value == None:
#         a = list()
#     a.append(value)
#     result[i.组名] = a
#
# result返回


# class
# 构造器  __init__(args)
# super(子类, self)
# A(B)
#
# 类
# main（）： 实例化， 调方法
# if __name__ == '__main__':
#   main()
# __init__   __name__
# 装饰器


def startEnd(fun):
    def wrap(name):
        print("start")
        fun(name)
        print("end")
    return wrap



@startEnd
def hello(name):
    print("hello {0}".format(name))

hello("ajing")

import os
# os.system("ipconfig")
# result = os.popen("ipconfig").read()
import json
# import commands   getstatusoutput
import sys
import random
# random.random()   0-1
# random.randint(a, b)
# random.sample(itertable, k)
# random.randrange(1, 100, 2)
import string

import logging
# logger = logging.getLogger(__name__)
# logger.debug

import hashlib
# m = hashlib.md5()
# src = "asdfdas"
# m.update(bytes(src))
# m.hexdigest()

from datetime import datetime
# datetime.now()
# datetimie.year  month  day  hour minute seconds
# datetime.now().strptime("%Y-%m-%d")

import time
# time.time()
# time.sleep(10)

from io import StringIO, BytesIO
# s = StringIO()
# s.write("hello world")
# s.getvalue()
# s.truncate(0)