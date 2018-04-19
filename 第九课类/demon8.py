#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 22:02
# @Author  : lingxiangxiang
# @File    : demon8.py



class JinCinCount(object):
    def __init__(self, n):
        self.n = n
    def jc(self, n):
        result = 1
        if n == 0:
            return result
        else:
            for i in range(1, n+1):
                result *= i
            return result
    def count(self):
        count = 0
        for i in range(0, int(self.n) + 1):
            count += self.jc(i)
        print("count = {0}".format(count))

def main():
    n = input("Please inpurt a number: ")
    jinCinCount = JinCinCount(int(n))
    jinCinCount.count()

if __name__ == "__main__":
    main()





