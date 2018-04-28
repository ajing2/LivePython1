#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/17 17:42
# @Author  : lingxiangxiang
# @File    : regex_test.py
import codecs
import os
import re

with codecs.open(r'ga10.wms5.jd.com.txt') as f1:
    a = re.compile(r'(\s*upstream\s+(\S+)\s*{(\s+server\s+.*\n)+})')
    result = a.findall(f1.read())
    if not os.path.exists('upstream'):
        os.mkdir('upstream')
    os.chdir('upstream')
    for x, y, z in result:
        with codecs.open('{0}.upstream.conf'.format(y.split('.')[0]), 'w') as up_file:
            up_file.write(x)
    os.chdir('..')
with codecs.open(r'ga10.wms5.jd.com.txt') as f:
    pattern = re.compile('(\s*location\s*[~]*\s*\S+\s{[^}]+proxy_pass\s+http://(\S+)\s*})')
    location = pattern.findall(f.read())
    if not os.path.exists('location'):
        os.mkdir('location')
    os.chdir('location')
    for x, y in location:
        # print(y.split('/')[0].split(';')[0])
        location_file = y.split('.')[0]
        # print(location_file)
        # print('{0}.location.conf'.format(location_file))
        with codecs.open('{0}.location.conf'.format(location_file), 'w') as lo_file:
            lo_file.write(x)



