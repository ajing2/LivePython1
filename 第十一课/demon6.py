#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 22:17
# @Author  : lingxiangxiang
# @File    : demon1.py
import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.printable)
# print(string.punctuation)
# print(string.hexdigits)
#


print("".join(random.sample(string.ascii_letters + string.digits, 4)))
