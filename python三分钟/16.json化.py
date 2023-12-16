# -*- coding: utf-8 -*-
# @File : 16.json化.py
# @Author : 阿波
# @Time : 2023/9/3 13:45
# @Software: PyCharm
food = [
    {'name': 'pizza', 'origin': 'Italy'},
    {'name': 'hamburger', 'origin': 'UK'},
]
import json
print(json.dumps(food,indent=4))


class Food(dict):
    def __init__(self, name, origin, calories, price):
        dict.__init__(self, name=name, origin=origin, calories=calories, price=price)
        self.name = name
        self.origin = origin
        self.calories = calories
        self.price = price

    def to_json(self):
        return self.__dict__


food1 = Food('胡辣汤', '山东', 25, 2)
food2 = Food('油条', '山东', 88, 1)
food3 = Food('豆腐脑', '山东', 35, 2.5)
food4 = Food('焖饼', '山东', 65, 10)
food1.price = 999

recommend = [vars(food1), vars(food2), vars(food3), vars(food4)]

import json

recommend_json = json.dumps(recommend, indent=4, ensure_ascii=False)
print(recommend_json)
