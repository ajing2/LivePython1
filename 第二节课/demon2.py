#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 21:57
# @Author  : lingxiangxiang
# @File    : demon2.py

# 链表和数组      数据结构中的内容
# 列表简单理解成数组
m = ["11.11", "2", "3", "a", "b", "c", "True"]

# m.append()
# m.reverse()
print(m.sort())
print(m)
print(m.pop(2))
print(m)
print(m.index("True"))
m.insert(2, "lingxiangxinag")
print(m)


a = list()
for i in range(1, 10):
    a.append(i)
print(a)

# b = list()
# b += [i for i in range(1, 10)]
# print(b)


b = ["a", "b", "c"]
a = (1, 2, 3, 1, 5, 6)
print(a.index(5))
print(a.count(1))

c = tuple(b)
print(c)


# 总结：
# ""   字符串
# 字符串的方法：
# find()  查找
# replace()   替换
# strip()    前后去空格
# join(可迭代对象)      集成
# split()     分割
# format()    字符串格式化

# []    列表     list()
# 列表常用的方法
# append()    屁股后追加
# pop()     最后删除，返回值是删除的那个元素
# index(x)    返回元素的下标
# remove(x)     删除元素
# sort()      list排除
# reverse()     反序
# [:]     分片，前开后闭
# 下标元素从0开始
# ()    元组     tuple()
# "".     字符串的方法
# [].      列表的方法
# ().index(x)    ().count(x)
