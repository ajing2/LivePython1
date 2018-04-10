#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 20:50
# @Author  : lingxiangxiang
# @File    : demon2.py
'''

ABCD乘9=DCBA，A=? B=? C=? D=? 答案：a=1,b=0,c=8，d=9      1089*9=9801

'''

for A in [1]:
    for B in range(0, 10):
        for C in range(0, 10):
            for D in [9]:
                if ((1000* A + 100*B + 10*C + D)*9 == 1000*D + 100*C + 10*B + A ):
                    print("A = {0}".format(A))
                    print("B = {0}".format(B))
                    print("C = {0}".format(C))
                    print("D = {0}".format(D))
                    print("{0}{1}{2}{3}x9={3}{2}{1}{0}".format(A, B, C, D))



