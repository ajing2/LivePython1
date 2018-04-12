#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 20:50
# @Author  : lingxiangxiang
# @File    : demon1.py

'''
文件操作
参数1： 文件名，可以是文件的绝对路劲
参数2： option  r 读  w 写   b二进制   a追加
'''


# 全局申明
import codecs

ENCODEING = "utf-8"


# 读取文件内容
fr = open("1.txt", "rb")
# for i, line in enumerate(fr.readlines()):
#     print("第{0}行内容为：{1}".format(i, line))
print(fr.readline())
print(fr.tell())
print(fr.readline())
print(fr.tell())
fr.seek(-3, 2)
print(fr.tell())

print(fr.name)
# print(fr.encoding)
print(fr.closed)



# print(fr.read())
fr.close()
print(fr.closed)


# 写入文件内容
fw = open("2.log", "w", encoding=ENCODEING)
fw.write("hello wolrd\n你咋不上天呢？\nno 作 no die!\n")
fw.truncate(10)
fw.close()



# 文件对象f常用的操作方法
# read()       把文件的所有内容都读取出来，返回一个字符串
# write(data)  把字符串data写入到文件中，只接受字符串参数
# fr.readline()   每次读取文件一行数据，返回每行的字符串数据
# fr.readlines()  读取文件内容，返回一个list，每一行是一个元素
# fr.name    文件名字
# fr.fileno()   文件描述符
# fr.close()    关闭文件
# fr.encoding    文件编码
# fr.closed    返回bool值， 判断文件是否已经关闭
# fr.seek(offset, whence)  offset偏移量正数向后偏移，负数向前偏移   whence 0 开头，1 现在位置  2 代表结尾
# fr.tell()       返回文件光标位置
# fr.truncate(size)   只有写文件才可以用，清空文件,size表示清空到什么地方.
# help(fr.seek)  控制文件光标，文件需要使用b方式打开，



print("#############################")
with codecs.open("1.txt", "r", encoding=ENCODEING) as f:
    print(f.read())



