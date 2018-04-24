#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 21:37
# @Author  : lingxiangxiang
# @File    : demon4.py


'''

sys

'''


import sys
print(sys.argv[1])
print(sys.argv[2])
print(sys.stdout)
sys.stdout.write("allalallala")

f = open("1.log", "w")
sys.stdout = f
print("hello world")