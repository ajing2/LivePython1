#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 21:20
# @Author  : lingxiangxiang
# @File    : demon3.py


number = input("Please input a number: ")
if int(number) > 0:
    print("{0} 是正数！".format(number))
elif int(number) < 0:
    print("{0} 是负数！".format(number))
else:
    print("输入的数字等于{0}".format(number))

