# -*- coding: utf-8 -*-
# @File : 6.循环访问索引.py
# @Author : 阿波
# @Time : 2023/9/2 16:37
# @Software: PyCharm
scores = [99, 96, 93, 85, 78, 66, 58]
for i,j in enumerate(scores,start=1):
    print(i,j)