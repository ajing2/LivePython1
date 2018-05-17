#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 20:35
# @Author  : lingxiangxiang
# @File    : demon1.py
import redis

r = redis.Redis(host="192.168.48.136", port=6379, db=0)
print(r)
print(r.keys())
print(r.get("aaa").decode("utf-8"))

# 字符串操作
# get(key)
# set(key, value)
# mget(k1, k2, k3, k4)
# mset(k1=v1, k2=v2)

# list的操作
# 左边添加 lpush(name, value)
# 右边添加 rpush(name, value)
# 插入  linsert(name, where, refvalue, value)
# 左边删除  lpop(name)
# 通过分片取list中的值  lrange(name, start, end)
# 修改list中的某个值   lset(name, index, value)
# 删除指定的值    lrem(name, value, num)   num默认为0， 删除所有，num=2 从左往右删除2个元素，num=-1从右往左删除两个元素

r.lpush("testlist1", 1)
r.lpush("testlist1", 2, 3, 4)
print(r.lrange("testlist1", 0, -1))


# set操作
# 增加  sadd(name, values)
# 获取  scard(name)
# 删除  spop(name) s.srem(name, value)
# 并集  sunion(keys)      例如：suniion("a", "b", "c")
# 交集  sinter(key)


# hash  主要要掌握string和hash的操作
# 获取key的详细内容   hgetall(name)
# 设置单个元素   hset(name, key, value)
# 设置多个元素   hmset(name, {"key": "value"})
# 获取单个元素   hget(name, key)
# 获取多个元素   hmget(name, keys)
# 获取多有的key  hkeys(name)
# 获取多有的value  hvals(name)
# 判断key是否存在   hexists(name, key)
# 删除key     hdel(name, keys)
# 获取长度     hlen(name)
r.hset("testhash", "k1", "v1")
print(r.hget("testhash", "k1"))
print(r.hgetall("testhash"))

r.hmset("testhash111", dict(k1="v1", k2="v2", k3="v3"))
print(r.hgetall("testhash111"))


# 其他常用的操作,适用于所有类型
# r.keys()   查看所有的key
# r.delete(names)   删除keys
# r.exists(name)   判断是否存在
# r.rename(src, dst)  新替旧
# r.expire(name, time)  设置超时时间
# r.type(name)    查看name属于哪种redis数据类型
# r.move(name, db)  把name从原理的db移动到db库下面
# r.flushall()     删除所有key
