#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 22:04
# @Author  : lingxiangxiang
# @File    : demon2.py

'''

函数定义（声明）：
以关键字def开头，函数名， 参数：回车缩进
def function(arg1, arg2, ……):
    pass

函数的就是一种封装的思想，把细小的功能或者可以缩小的功能封装成一种函数

函数的调用：
函数名直接传入参数就可以

function（1， 2， 3）

arg1， arg2   形参
1， 2， 3     实参



def fun(a, *args, **kwargs):
    pass


*args   代表什么意思    list
*goushi
**kwargs 代表什么意思   dict
**lese

fun(1, 2, 3, 4, 5 ,a=1, b=2)

x, y, z, = 1, 2, 3

a = 1
args = 2, 3, 4, 5   list 一一对应过来
kwars ={"a": 1, "b": 2}   dict  一一对应过来


匿名函数：
add = lambda x, y: x+y

def add(x, y):
    return x+y
'''



def jc(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

def main():
    n = 10
    count = 0
    for i in range(0, n+1):
        count += jc(i)
    print("count = {0}".format(count))




if __name__ == '__main__':
    main()

