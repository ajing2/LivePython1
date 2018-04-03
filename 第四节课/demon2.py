#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 21:01
# @Author  : lingxiangxiang
# @File    : demon2.py

age = input("Please input your age: ")
# print(type(age))
if age.strip():
    if age.isdigit():
        if int(age)>=18:
            print("你是一个成年人！")
        else:
            print("你还是一个小屁孩！")
    else:
        print("你输入的不是数字")
else:
    print("你输入的只有空格")


