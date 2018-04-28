#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 21:54
# @Author  : lingxiangxiang
# @File    : demon1.py

'''<h1>xxx</h1>   查看不同匹配规则的效率'''

import re
import timeit
# print(timeit.timeit(setup='''import re; reg = re.compile('<(?P<tagname>\w*)>.*</(?P=tagname)>')''', stmt='''reg.match('<h1>xxx</h1>')''', number=1000000))
# print(timeit.timeit(setup='''import re''', stmt='''re.match('<(?P<tagname>\w*)>.*</(?P=tagname)>', '<h1>xxx</h1>')''', number=1000000))

s = "ab<h1>xxx</h1>dsafasdf<html>sdfads</html>"
reg = re.compile(r"(<(?P<tag>\w+)>(.*)</(?P=tag)>)")
print(reg.match(s))
print(reg.search(s).group(3))
print(reg.findall(s))
# print(reg.findall(s)[1])
# print(reg.findall(s)[2])
# reg.split(s)
# reg.findall(s)
# reg.groups(s)


x = '1one2two3three4four'
reg1 = re.compile("\d")
print(reg1.findall(x))
print(reg1.split(x))
