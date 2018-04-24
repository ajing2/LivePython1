#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 22:01
# @Author  : lingxiangxiang
# @File    : demon5.py
'''
random
随机模块
random.randint(a, b)

'''
import random

print(random.randrange(1, 100, 2))
print(random.sample([1, 2, 3, 4, 5, 6, 7], 2))

class NumberCount(object):
    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.number3 = 0
        self.number4 = 0
        self.number5 = 0
        self.number6 = 0
    def count(self):
        for i in range(1, 6001):
            number = random.randint(1, 6)
            if number == 1:
                self.number1 += 1
            if number == 2:
                self.number2 += 1
            if number == 3:
                self.number3 += 1
            if number == 4:
                self.number4 += 1
            if number == 5:
                self.number5 += 1
            if number == 6:
                self.number6 += 1
    def getResult(self):
        print("1出现的次数: {0}".format(self.number1))
        print("2出现的次数: {0}".format(self.number2))
        print("3出现的次数: {0}".format(self.number3))
        print("4出现的次数: {0}".format(self.number4))
        print("5出现的次数: {0}".format(self.number5))
        print("6出现的次数: {0}".format(self.number6))

if __name__ == "__main__":
    numberCount = NumberCount()
    numberCount.count()
    numberCount.getResult()