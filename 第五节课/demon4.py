#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 21:57
# @Author  : lingxiangxiang
# @File    : demon4.py
'''
0! +1！ +2！ + 3！ +4! + 5! + n!
1 + 1 + 2 + 6 + …… + n*(n-1)*(n-2)……*1

'''

def jc(n):
    result = 1
    if n == 0:
        return result
    else:
        for i in range(1, n+1):
            result *= i
        return result


n = input("Plese inpurt number n:")
count = 0
for i in range(0, int(n)+1):
    count += jc(i)

print("count = {0}".format(count))



