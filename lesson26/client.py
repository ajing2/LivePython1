#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 21:27
# @Author  : lingxiangxiang
# @File    : client.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1', 6666)
s.connect(address)
flage = 1
print("start client!")
while flage:
    word = input("word: ")
    if word == "exit":
        flage = 0
    s.sendall(word.encode('utf-8'))
    data = s.recv(2048)
    print("RECV: {0}".format(data.decode('utf-8')))

s.close()