#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 21:52
# @Author  : lingxiangxiang
# @File    : masterApp.py
import codecs
import json

import commands

def publicKey(ipaddr):
    with codecs.open('/tmp/{0}.txt'.format(ipaddr), 'w') as f:
        f.write("{0} ansible_ssh_pass=123456".format(ipaddr))
    resultBean = dict()
    cmd = "ansible -i /tmp/{0}.txt all -m script -a '/srv/salt/_shell/installpub.sh'".format(ipaddr)
    status, output = commands.getstatusoutput(cmd)
    if status == 0:
        resultBean['code'] = 0
        resultBean['message'] = 'success'
        resultBean['data'] = output
        return json.dumps(resultBean)


def installMinionid():


