#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 21:18
# @Author  : lingxiangxiang
# @File    : demon2.py
'''
module 和目录的区别，看是否有__init__.py文件
讲一些，我们常用的module，
'''
from 第十课.demon1 import test

if __name__ == '__main__':
    result = test()
    print(result)