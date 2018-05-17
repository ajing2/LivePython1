#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 21:36
# @Author  : lingxiangxiang
# @File    : demon2.py
'''pip install pytyhon-memcached'''
import memcache

mc = memcache.Client(['192.168.48.136:12000'])
print(mc)
mc.set("aaa", "hello world")
print(mc.get("aaa"))

# set(key, value)
# get(key)
# repalce(key, new_value)
# set = add + replace()
# delete(key)
# get_multi([k1, k2, k3])
# delete_multi([k1, k2, k3])
# set_multi({"k1": "v1", "k2": "v2"})
# append(k, appendvalue)
# prepend(k, prependvalue)
mc.append("aaa", " 321")
print(mc.get("aaa"))
mc.prepend("aaa", "123 ")
print(mc.get("aaa"))
print(mc.stats)




# mc.add("mctestadd", "nihaoma")
# print(mc.get("mctestadd"))

