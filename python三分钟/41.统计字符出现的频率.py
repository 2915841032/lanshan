# -*- coding: utf-8 -*-
# @File : 41.统计字符出现的频率.py
# @Author : 阿波
# @Time : 2023/9/4 21:09
# @Software: PyCharm
from collections import Counter

# 统计一下字母出现频率
result = Counter("Banana")
print(result)

# 统计一下数字出现频率
result = Counter([1, 2, 1, 3, 1, 4, 1, 5, 1, 6])
print(result)
