# -*- coding: utf-8 -*-
# @File : 44.连接数据库2.py
# @Author : 阿波
# @Time : 2023/9/9 13:10
# @Software: PyCharm

import datetime
import pymysql
import numpy as py
import pandas as pd

db = pymysql.connect(host='10.101.2.36',            #要连接的主机地址
                           user='selxxx',           #用于登录的数据库用户
                           password='selxxx@123',   #用户密码
                           database='xxx_loan',     #要连接的数据库
                           port=3306,               #连接的端口
                           charset='',              #字符编码
                           use_unicode=None,        #是否使用unicode编码
                           connect_timeout=10000    #连接超时时间
                    )
cursor = db.cursor()                                #创建一个游标
#版本一：直接在程序中写sql
sql_recent_5d_sx = '''
    select
        appl_date,
        count(
                distinct 
                case when u.appl_type=1 
                then loan_appl_no 
                else null 
                end
                ) as `申请量`,
        count(
                distinct 
                case 
                when u.appl_type=1 
                and OUT_TEMPDECISION = 'PASS'
                then loan_appl_no 
                else null 
                end
                ) as `系统自动通过量`
    from table
'''                                #sql脚本
cursor.execute(sql_recent_5d_sx)   #执行sql语句
sql_result = cursor.fetchall()     #取出操作返回的所有的行

#版本二：把sql存到txt文档中
sql_path_recent_5d_sx = r'C:\Users\xzy\recent_5day_sx.txt'               #标记sql存储路径
sql_recent_5d_sx = open(sql_path_recent_5d_sx, encoding='utf-8').read()  #打开sql脚本并读取sql
cursor.execute(sql_recent_5d_sx)                                         #执行sql语句
sql_result = cursor.fetchall()                                           #取出操作返回的所有的行




data_recent_5d_yx = pd.DataFrame(sql_result)  #把sql结果转成数据框
data_recent_5d_yx.columns = [
'date',
'用信申请笔数',
'用信通过笔数',
'用信通过率',
'用信金额',
'白条支付占比',
'白条提现占比',
'白条外部用款占比',
'先息后本占比',
'等额本息占比'
]                                            #给数据框添加列名
data_recent_5d_yx = data_recent_5d_yx.T      #把数据框转置一下
data_recent_5d_yx.columns = data_recent_5d_yx.iloc[0] #给数据框添加行名
data_recent_5d_yx = data_recent_5d_yx.iloc[1:]        #删除第一行
#data_recent_5d_yx
for i in data_recent_5d_yx.columns:
    data_list_2.remove(i)
for i in data_list_2:
    data_recent_5d_yx[i] = 0
data_recent_5d_yx_f = data_recent_5d_yx[data_list_0]  #最终结果