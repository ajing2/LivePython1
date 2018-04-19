#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 21:00
# @Author  : lingxiangxiang
# @File    : demon4.py
'''
继承  spuer
重写
调用：  先去找子类中的方法，如果子类中找不到对应的方法，就是父类中找
多继承：如果父类中都有该方法，那么先继承谁， 就用谁的方法。
'''

class Animal(object):
    def __init__(self, name):
        print("你现在正在初始化一个Animal")
    def run(self):
        print("Animal can run.")

class Bird(Animal):
    def __init__(self):
        print("bird")
    def fly(self):
        print("Bird can fly.")

class Cat(Animal):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        super(Cat, self).__init__(self.name)
        print("我是一只猫，啦啦啦啦")
    def jiao(self):
        print("miao miao miao miao")
    def run(self):
        print("我是一只猫，会上树来会跑路.")


class BianYi(Cat, Bird):
    pass


# animal = Animal()
# cat = Cat()
# cat.run()

# bianYi = BianYi()

cat = Cat("mao", "man")


