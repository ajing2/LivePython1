#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 21:25
# @Author  : lingxiangxiang
# @File    : demon3.py

import json

test = '[{"a": 1, "aa": 11, "aaa": 111}, {"b": 2, "bb": 22, "bbb": 222}, {"c":3}]'
test2 = '''{'aaa': 111, 'bbb': 222}'''
print(type(test))

# json.dumps()
newTest = json.loads(test)
print(type(newTest))
print(newTest[0]["a"])

xxx = json.dumps(newTest)
print(type(xxx))

yyy = str(newTest)
print(type(yyy))

print(type(json.loads(xxx)))
# print(type(json.loads(yyy)))


# print(test2)
# print(type(test2))
# result = json.loads(test2)
# print(result)