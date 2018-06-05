#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 20:22
# @Author  : lingxiangxiang
# @File    : demon1.py


import socket

host = "www.baidu.com"
port = 443

ip = socket.gethostbyname(host)
print(ip)

address = (ip, port)

try:

    s = socket.socket()

    s.connect(address)
    request = "GET / HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n"
    s.sendall(request.encode("utf-8"))
    res = s.recv(80960)
    if res:
        print(res)
    else:
        print("visit {0} error".format(host))
except Exception as e:
    raise e


