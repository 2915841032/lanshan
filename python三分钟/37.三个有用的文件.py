# -*- coding: utf-8 -*-
# @File : 37.三个有用的文件.py
# @Author : 阿波
# @Time : 2023/9/4 10:33
# @Software: PyCharm
import pprint
import random

# print(dir(random))

pprint.pprint(dir(random))
help(random.randint)

name = '张三'
print(id(name))

name1 = '张三'
print(id(name1))

name2 = '张三'
print(id(name2))
