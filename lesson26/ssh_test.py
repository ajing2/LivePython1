#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 21:59
# @Author  : lingxiangxiang
# @File    : ssh_test.py
'''
ssh
'''

import paramiko


client = paramiko.SSHClient()
# 允许链接不在know_host文件中的主机
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

client.connect('192.168.48.136', 22, username='root', password='123456', timeout=5)
while 1:
    cmd = input('[root@localhost ~]#')
    stdin, stdout, stderr = client.exec_command(cmd)
    for std in stdout.readlines():
        print(std)
client.close()