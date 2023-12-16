# -*- coding: utf-8 -*-
# @File : 8.安全删除字典中的key.py
# @Author : 阿波
# @Time : 2023/9/2 18:12
# @Software: PyCharm
my_dict={'lk':12,'JAPAN':13,"rt":34}
my_dict.pop('JAPA', None)
print(my_dict)