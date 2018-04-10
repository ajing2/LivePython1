#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 20:33
# @Author  : lingxiangxiang
# @File    : demon1.py

'''
判断一个字符串数字有多少个
字母有多少个
空格有多少个
其他字符

'''



while 1:
    strings = input("Please inpur a string(quit will be exit):")
    alpha, dig, space, other = 0, 0, 0, 0
    if strings.strip() == "quit":
        exit(1)
    for i in strings:
        if i.isdigit():
            dig += 1
        elif i.isspace():
            space += 1
        elif i.isalpha():
            alpha += 1
        else:
            other += 1
    print("alpha = {0}".format(alpha))
    print("dig = {0}".format(dig))
    print("space = {0}".format(space))
    print("other = {0}".format(other))