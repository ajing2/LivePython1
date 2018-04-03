#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 20:56
# @Author  : lingxiangxiang
# @File    : demon1.py

'''
    这是一个测试程序
'''
"""
    hello world
"""

# java  c   都需要先声明，在实例化
# int a;  a = 10;

a = 10
b = "hello world"
c = 11.961
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(int(c))

print(round(c, 1))


# 字符串常用的方法：
# strip                  字符串过滤空格，有事没事，你用一下,只能过滤前和尾的空格
# replace(old, new)      字符串内容老的替换新的
# find(sub)              字符串中查找sub字符串的内容，如果找到，返回自字符串的下标，否则返回-1
# format                 字符串格式化
# split                  切割字符串
print(" a1 b 2c3d4".strip())
print("a1b1c1d1".split("1"))
print("asdfasjdfas".startswith("asd"))
name = "lingxiangxiang"
shang = 18
print("hello " + name)
print("%s's age is: %d" %(name, shang))

str1 = "a1b1c1d1"
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])




a = ["a", "b", "c", "d", "e"]
print("------".join(a))
print(a)
"".split()



a = "a1b2c3d4"
print(a)

