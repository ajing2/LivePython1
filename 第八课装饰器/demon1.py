#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 21:09
# @Author  : lingxiangxiang
# @File    : demon1.py


def hello():
    print("hello world")


#  !!!!!!!start!!!!!!!!
#  hello world   (hello)
# !!!!!!!!end!!!!!!!!!


a = hello()
print("aaaaaaaaaaaaaaaaaaaaa")
b = hello

# a 代表什么     hello函数把返回这给到a  None
# b 代表什么     b是一个函数, b()相当于hello()
b()
