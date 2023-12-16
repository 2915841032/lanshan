# -*- coding: utf-8 -*-
# @File : 15.序列化.py
# @Author : 阿波
# @Time : 2023/9/2 20:40
# @Software: PyCharm
class Food:
    def __init__(self, name, origin, calories, price):
        self.name = name
        self.origin = origin  # 产地
        self.calories = calories  # 卡路里
        self.price = price


print('...此处省略2500行推荐算法代码...')
food1 = Food('胡辣汤', '山东', 25, 2)
food2 = Food('油条', '山东', 88, 1)
food3 = Food('豆腐脑', '山东', 35, 2.5)
food4 = Food('焖饼', '山东', 65, 10)

recommend = [food1, food2, food3, food4]
import pickle
with open("foods.pickle", "wb") as out:
    pickle.dump(recommend, out)



with open("foods.pickle", "rb") as out:
    remote_recommend = pickle.load(out)

for i in remote_recommend:
    print(i.name)