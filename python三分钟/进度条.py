# -*- coding: utf-8 -*-
# @File : 进度条.py
# @Author : 阿波
# @Time : 2023/8/31 14:59
# @Software: PyCharm
import time
import progressbar

p = progressbar.ProgressBar()  # 实例化进度条
max_value = 100  # 满值100
p.start(max_value)

init_num = 0
n = 0
update_value = 1

while n < 100:
    p.update(n)  # 更新
    n += update_value
    time.sleep(0.1)

p.finish()