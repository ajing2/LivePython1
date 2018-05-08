#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 21:27
# @Author  : lingxiangxiang
# @File    : demon2.py
'''

create table 表名(
    列名 数据类型 not null
    ………………
);

create table Stdunet(
stdId int not null,
stdname varchar(100),
age int,
sex enum('M', 'F'),
score int);


'123'              varchar(10)
'123       '       char(10)

grant all privileges on *.* to 'user1'@'%' identified by '123456' with grant option;
你这个user1用户，只能对所有的库，所有的表进行增删改查等，没有对其他用户进行授权   user2就没法授权



'''