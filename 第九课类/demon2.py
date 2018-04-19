#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 20:38
# @Author  : lingxiangxiang
# @File    : demon2.py
'''
类， 面向对象一个很重要的载体

1. 类的定义
class StuentName(object):
    pass

2. 类里面一般都是由很多函数组成，函数的第一个参数默认都是self
如果需要全局变量，就在类的内部直接定义

3. 类的内部在调用函数或者调用变量的时候，必须使用self.变量   或者self.函数

self 代表的是类实例化以后的个体

4.类的实例化
实例化类的首字母小写作为实例，然后类实例化
studentName = StudentName();

5. 构造器

6. 继承
'''

class A(object):
    name = "ajing"
    def hello(self):
        print("hello {0}".format(self.name))
    def test(self):
        self.hello()
        print("This is test.")

a = A()
b = A()
