# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : create_table.py
# @Software: PyCharm
# @Time    : 2023/12/21 20:47


from feapder.db.mysqldb import MysqlDB

db = MysqlDB(ip='localhost', user_name='root', user_pass='root', db='py_spider')

create_table_sql = """
    create table wp_shop_info(
        id int primary key auto_increment,
        title varchar(255) default null,
        price varchar(255) default null
    );
"""
db.execute(create_table_sql)
