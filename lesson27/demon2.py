#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 20:34
# @Author  : lingxiangxiang
# @File    : demon2.py
'''
python -m http.server 80  python3

python -m SimpleHTTPRequest
'''


import http.server
import socketserver
port = 8000
host = '127.0.0.1'
address = (host, port)
# handle = SimpleHTTPRequest.SimpleHTTPRequestHandler
handle = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(address, handle) as httpd:
    print("server start")
    httpd.serve_forever()