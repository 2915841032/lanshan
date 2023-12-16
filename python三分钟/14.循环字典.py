# -*- coding: utf-8 -*-
# @File : 14.循环字典.py
# @Author : 阿波
# @Time : 2023/9/2 19:55
# @Software: PyCharm
scores = {'zhangsan': 98, 'lisi': 89, 'maishu': 96}

for i,j in enumerate(scores.items()):
    print(i,j[1])

