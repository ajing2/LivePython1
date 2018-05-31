#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 21:27
# @Author  : lingxiangxiang
# @File    : server.py
import socket

import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1', 6666)
s.bind(address)
s.listen(10)
print("start server!")
while 1:
    try:
        conn, addr = s.accept()
        if conn:
            print("recv client from {0}".format(addr))
            while 1:
                data = conn.recv(2048)
                print("recv data: {0}".format(data.decode('utf-8')))
                conn.sendall(data.decode('utf-8').upper().encode('utf-8'))
        else:
            time.sleep(5)
    except Exception as e:
        conn.close()
