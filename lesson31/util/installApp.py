#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 21:46
# @Author  : lingxiangxiang
# @File    : installApp.py



def nginx():
    resultBean = dict()
    __salt__['cp.get_file']("salt:_shell/app/nginx.sh /usr/local/src/installnginx.sh")
    jid = __salt__['cmd.async']
    cmd = "sh /usr/local/src/installnginx.sh"
    status, output = commands.getstatusoutput(cmd)
    if status == 0:
        resultBean['code'] = 0
        resultBean['message'] = 'success'
        resultBean['data'] = output
    else:
        resultBean['code'] = -1
        resultBean['message'] = 'install nginx error'
        resultBean['data'] = output
    return resultBean

def tomcat():
    pass

def keepalived():
    pass

def lvs():
    pass

def jdk():
    pass

def mysql():
    pass

def zookeeper():
    pass

def redis():
    pass

