#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 21:51
# @Author  : lingxiangxiang
# @File    : demon5.py


while 1:
    age = input("Please input your age: ")
    # print(type(age))
    if age.strip():
        if age.isdigit():
            if int(age) >= 18:
                print("你是一个成年人！")
                break
            else:
                print("你还是一个小屁孩！")
                break
        else:
            print("你输入的不是数字, 请重新输入： ")
            continue
    else:
        print("你输入的只有空格, 请重新输入：")
        continue


