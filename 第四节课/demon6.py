#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 21:57
# @Author  : lingxiangxiang
# @File    : demon6.py

# for i in range(1, 10):
#     print("{0} x {1} = {2}".format(i, i, i*i))


#1  1x1=1
#2  1x2=2 2x2=4
#3  1x3=3 2x3=6 3x3=9

# a x b = a*b
# a最小是最小为1， 最大为行号
# b等于行号

for b in range(1, 10):
    for a in range(1, b+1):
        print("{0}x{1}={2}".format(a, b, a*b), end=" ")
        if a == b:
            print()

