# -*- coding: utf-8 -*-
# @File : 24.获取列表中最大或最小的n个数字.py
# @Author : 阿波
# @Time : 2023/9/4 19:47
# @Software: PyCharm
# 获取列表中最大或最小的n个数字
scores = [51, 33, 64, 87, 91, 75, 15, 49, 33, 82]


# 先排序，再切片。
scores.sort(reverse=True)
print(scores[0:3])

import heapq
print(heapq.nlargest(3, scores))  # [91, 87, 82]
print(heapq.nsmallest(5, scores))  # [15, 33, 33, 49, 51]

print(help(heapq.nlargest))