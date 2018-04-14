#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 20:38
# @Author  : lingxiangxiang
# @File    : demon3.py
'''
高阶函数    装逼函数
都是可以通过代码逻辑实现的。
都是可以通过代码逻辑实现的
但是你写的函数的负责程序，或者算法不一定有人家内置的好
'''
from functools import reduce


def f(x):
    return x*x

print(map(f, [1, 2, 3, 4]))
print(list((map(f, [1, 2, 3, 4]))))
for i in map(f, [1, 2, 3, 4]):
    print(i)



def testMap(fun, iter):
    l = list()
    for i in iter:
        l.append(fun(i))
    return l


print(testMap(f, [1, 2, 3, 4]))



def add(x, y):
    return x+y

reduce(add, [1, 2, 3, 4, 5])
# 1, 2   = 3
# 3, 3   = 6
# 6, 4   = 10
# 10, 5   = 15



# 唯一用的比较多的，就是sorted
# sorted(iterable, key, reverse)
# iterable  一个可迭代的对象
# key 对什么进行排序
# reverse  bool类型，如果为true为反序， 默认为false
# 返回值是一个list
print(sorted([1, 4, 342, 3, 45, 76, 435, 34], reverse=True))


m = dict(a=1, c=10, b=20, d=15)
print(m)
print(sorted(m.items()))
print(sorted(m.items(), key=lambda x: x[0]))
print(dict(sorted(m.items(), key=lambda x: x[1])))
# print(sorted(m.items(), key = lambda d:d[1], reverse = True))

# for i in m:
#     print(i)
#
# for i in m.items():
#     print(i)



# 字典有三种初始化的方法
d1 = dict(a=1, b=2)
d2 = {"a": 1, "b": 2}
d3 = dict([("a", 1), ("b", 2)])
print(d1, d2, d3)
