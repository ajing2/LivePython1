#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 20:52
# @Author  : lingxiangxiang
# @File    : test.py
from lesson31.util.saltapi import SaltServer

saltServer = SaltServer()

# result1 = saltServer.runModules('192.168.48.129', 'cp.get_file', ['salt://_shell/app/nginx.sh', '/usr/local/src/installnginx.sh'])
# print(result1)
# result2 = saltServer.runModules('192.168.48.129', 'installApp.nginx')
# print(result2)
# result2 = saltServer.runRunner('manage.status')
# print(result2)
#
# result1 = saltServer.runRunner('masterApp.publicKey', ipaddr='192.168.48.133')
# print(result1)
result2 = saltServer.runRunner('masterApp.installMinionid', ipaddr='192.168.48.133')
print(result2)

