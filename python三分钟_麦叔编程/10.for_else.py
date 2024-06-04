# -*- coding: utf-8 -*-
# @File : 10.for_else.py
# @Author : 阿波
# @Time : 2023/9/2 18:29
# @Software: PyCharm
foods = ['大葱', '大蒜', '生姜', '萝卜', '青菜', '辣椒']
for f in foods:
  # 叔就喜欢吃青菜
  if f == '青菜':
    print('我要点青菜！')
    break
else:
    print('没我喜欢的，今天我减肥！')
