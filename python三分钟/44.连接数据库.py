# -*- coding: utf-8 -*-
# @File : 44.连接数据库.py
# @Author : 阿波
# @Time : 2023/9/9 12:14
# @Software: PyCharm

# 第一种读取方式
import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='文',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
sql = "SELECT * FROM 代理ip limit 3"
cursor.execute(sql)
results = cursor.fetchall()  # 获取所有结果
for row in results:
    # 处理每一行数据
    print(row)
cursor.close()
connection.close()


import pandas as pd

# 第二种读取方式
conn = pymysql.Connect(host='localhost', user='root', passwd='root', db='文',cursorclass=pymysql.cursors.DictCursor)
# 建立连接，host中填mysql服务器所在的主机的ip，user中填为用户名，passwd中填密码，db中填数据库名
sql = ''' select * from  代理ip limit 3'''
date = pd.read_sql_query(sql, conn)
print(date)


# 第三种读取方式
import pandas as pd
from sqlalchemy import create_engine
#
conn = create_engine('mysql+pymysql://root:root@localhost:3306/world',encoding='utf8')
#建立连接，user替换为用户名，passwd替换为密码，ip替换为mysql服务器所在的主机的ip，db中填数据库名
sql = ''' select * from  city limit 3'''
date = pd.read_sql_query(sql, conn)
print(date)


# 利用pandas把数据导入到数据库

conn = create_engine('mysql+pymysql://root:root@localhost:3306/world',encoding='utf8')
#建立连接，user替换为用户名，passwd替换为密码，ip替换为mysql服务器所在的主机的ip
data=pd.read_csv("./csv目录/ip数据.csv")
data.to_sql("ip_data", conn, if_exists='replace', index=False)
print('ok')
#

# 一行一行追加写入少量数据
import pandas as pd
import pymysql.cursors
from sqlalchemy import create_engine

#读取数据
conn = create_engine('mysql+pymysql://root:root@localhost:3306/world',encoding='utf8')
jxb_sx_head3 = pd.read_sql('''select * from ip_data limit 3''',conn)
#
# #写入数据
conn = create_engine('mysql+pymysql://root:root@localhost:3306/test',encoding='utf8')
jxb_sx_head3.to_sql("jlkj_cs", conn, if_exists='replace', index=False)
print('ok1')
#
#单条插入数据
conn = pymysql.Connect(host='localhost', user='root', passwd='root', db='test')
cursor = conn.cursor()
cursor.executemany("insert into jlkj_cs values(%s,%s,%s,%s,%s)", [('36.91.148.37','8080','黑龙江省鹤岗市','高匿代理','2023年03月26日22验证'),('36.91.148.37','8080','黑龙江省鹤岗市','高匿代理','2023年03月26日22验证')])
conn.commit()
print('ok2')
#

# # 批量追加写入数据
conn = create_engine('mysql+pymysql://root:root@localhost:3306/test',encoding='utf8')
#建立连接，user替换为用户名，passwd替换为密码，ip替换为mysql服务器所在的主机的ip
data=pd.read_csv("./csv目录/ip数据.csv")
data.to_sql("ip_data", conn, if_exists='append', index=False,index_label=False)
print('ok3')

