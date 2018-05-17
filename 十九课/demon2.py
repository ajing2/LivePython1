#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 22:01
# @Author  : lingxiangxiang
# @File    : demon2.py

# pip install redis
import redis

r = redis.Redis(host='192.168.48.136', port=6379)
print(r.get("aaa").decode())
r.set('mystring', 'good good study, day day up!')
print(r.get("mystring"))

r.mset(name1="ling", name2="ajing", name3="shang")
print(r.mget("name1", "name2", "name3"))


