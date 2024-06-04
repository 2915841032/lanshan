# -*- coding: utf-8 -*-
# @File : 51.随机数真的是随机的吗.py
# @Author : 阿波
# @Time : 2023/9/10 15:09
# @Software: PyCharm
import random
import time
print(time.time_ns())
random.seed(time.time_ns())  # 注入种子数666

# 随机产生10个100以内的数
for n in range(10):
  print(random.randint(1, 100))