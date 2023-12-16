# -*- coding: utf-8 -*-
# @File : 32.参数的传递.py
# @Author : 阿波
# @Time : 2023/9/8 12:42
# @Software: PyCharm
class CoffeeRequirement:
    """咖啡需求，包含如下参数：产地，品牌，口味，大小，温度，甜度，研磨时间，是否手工制作"""

    def __init__(self, flavour, size, from_country, brand, temperature, sweet, time, hand_made):
        print(flavour, size, from_country, brand, temperature, sweet, time, hand_made)


def make_a_coffee(coffee_requirement):
    pass


requirement = CoffeeRequirement('卡布奇诺', 'XXXXL', '巴西', '星巴克', '66.6', '加糖', '60M', True)

make_a_coffee(requirement)
make_a_coffee(requirement)