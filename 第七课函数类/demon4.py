#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 21:34
# @Author  : lingxiangxiang
# @File    : demon4.py

'''

列表生成式
[exp for val in collection if condition]

生成器
方法一：
(exp for val in collection if condition)
方法二：

'''


def jgg():
    number = list()
    for i in range(1, 10):
        number.append(i)
    for A in [x for x in range(1, 10)]:
        for B in [x for x in range(1, 10) if x != A]:
            for C in [x for x in range(1, 10) if x != A and x != B]:
                for D in [x for x in range(1, 10) if x != A and x != B and x!= C]:
                    print("A = {0} B = {1}  C = {2} D = {3}".format(A, B, C, D))


# jgg()

a1 = (x for x in range(1, 10) if x%2==0)
print(a1)
# python2   a1.next()
print(next(a1))#python3 是直接调用next方法
print("##"*10)
for i in a1:
    print(i)

a2 = [x for x in range(1, 10) if x%2==0]
print(a2)


def test():
    a = 1
    for i in range(1, 10):
        yield i
        # return i
        a += 1
        # return i
#return和yield的区别
# yield 可以理解成return，但是比return多一些角色
# yiele 每次都返回，但是下一次取值时，从上一次yield的下一行开始
m = test()
print(m)