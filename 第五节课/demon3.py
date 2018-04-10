#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 21:07
# @Author  : lingxiangxiang
# @File    : demon3.py
'''

九宫格
1-9
                -------------
                | A | B | C |
                | D | E | F |
                | G | H | I |
                -------------
所有的横竖斜线加起来都等于15
A  1-9
B  1-9 除A
C  1-9 除A,B

'''

number = list()
for i in range(1, 10):
    number.append(i)
print(number)


count = 1
for A in number:
    a = number.copy()
    a.remove(A)
    for B in a:
        b = a.copy()
        b.remove(B)
        for C in b:
            c = b.copy()
            c.remove(C)
            for D in c:
                d = c.copy()
                d.remove(D)
                for E in d:
                    e = d.copy()
                    e.remove(E)
                    for F in e:
                        f = e.copy()
                        f.remove(F)
                        for G in f:
                            g = f.copy()
                            g.remove(G)
                            for H in g:
                                h = g.copy()
                                h.remove(H)
                                for I in h:
                                    if (A+B+C == D+E+F == G+H+I == A+D+G == B+E+H == C+F+I == A+E+I == G+E+C == 15):
                                        print('''
                                        第{9}种例子
                                        -------------
                                        | {0} | {1} | {2} |
                                        | {3} | {4} | {5} |
                                        | {6} | {7} | {8} |
                                        -------------'''.format(A,B,C,D,E,F,G,H,I,count))
                                        count += 1








