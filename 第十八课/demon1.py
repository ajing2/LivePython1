#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/13 20:04
# @Author  : lingxiangxiang
# @File    : demon1.py

'''
创建一个test库
create database test;
授权一个用户
grant all privileges on *.* to 'xiang'@'%' identified by '1qaz@WSX';
创建表
create table student(id int not null);
查询
select * from tabel_name where 条件1 and  条件2
增加
insert into table_name (id, name, age, sex, grander) values (1, 'ling', 25, 'M', 99), (2, 'ajing', 45, 'F', 88);
改
update table_name set id=10 where 条件判断
删除
delete from table_name  where 条件判断
drop table table_name

联合查询
select a.id, b.name from A a join B b on a.id=b.tid

创建索引
create index idx_库名_表名_列名1_列名2 (列名1， 列名2)

查看sql是否走索引
explain select * from student where name='ling'

链接数据库
Python2 使用的是MySQLdb
python3 使用的pymysql  pip安装

1. 创建链接和游标
注意：在mysql连接中，尽量使用一个连接，确保mysql的并发数
conn = pymysql.connect(host='', port=, user='', passwd='', db='')
cus = conn.curse()
2. 实行sql
sql = "select * from Student;"
cus.execute(sql)
cus.fetchone()  获取单个  返回值  tuple
cus.fetchall()  获取多个  返回值  list（单个元素是tuple）
cus.fetchmany(size=n)  获取多个
3. 关闭游标和连接
cus.close()
conn.close()
注意结合try exception finally的使用


SQLAlchemy
1. 创建引擎
engine = create_engine('mysql+pymysql://username:password@hostname:port/db')
2. 创建session
DBsession = sessionmaker(bind=engine)
session = DBsession()

3.创建表
a. 获得engine
b. metadata = MetaData(engine)
c. student = Table('表名', metadata, Colume('id', Integer, primary_key=True), Colume('name', String(50))
d. metadata.create_all()

4.增加
a. 先要有一个模型
Base = declarative_base(0
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), primary_key=True)

b. 导入模型类，实例化该类，
sutdent1 = Student(1, 'ling')
c. session.add(单实例)      session.add_all([实例1, 实例2])

5. 查询
filter和filter_by的区别
filter：可以使用>  < 等，但是列必须是： 表.列，   filter的等于号是==
session.query(Student).filter(Student.id>100)
filter 不支持组合查询
session.query(Student).filter(Studnet.id>100).filter(name='ling')

filter_by： 可以直接写列，不支持< >  filter_by 等于是==
session.query(Student).filter_by(id==10)
filter_by 可以支持组合查询
session.query(Student).filter_by(name='ling' and id='342')

select * from student where name like '%ling%';
模糊查询含有ling的关键字

模糊查询
session.query(Student).filter(Student.name like('%ling%'))

获取数据的时候有两个方法：
one()   tuple
all()   list(单个元素是tuple)
如果在查询中不写one(), 或者all()  出来的就是sql语句


6. 更新
1.  先查出来
2. 跟新一下类所对应的属性值就ok
3. session.commit()
student1 = session.query(Student).filter(Student.id=1001)
student1.name = "test"
session.commit()

7. 删除
1. 先查出来
2. 直接调用delete()方法就可以
3. 提交一下

8.统计， 分组，排序

统计：count()
只需要在查出来以后， 把one或者all替换成count()
统计有多少个

分组：group_by
查出来以后，把one或者all替换成group_by(属性)




'''