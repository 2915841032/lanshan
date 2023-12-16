# -*- coding: utf-8 -*-
# @File : 调试.py
# @Author : 阿波
# @Time : 2023/9/4 11:11
# @Software: PyCharm
from icecream import ic


def square_of(num):
    return num * num


ic(square_of(2))
ic(square_of(3))
ic(square_of(4))


class Dog():
    num_legs = 4
    tail = True


dog = Dog()
ic(dog.tail)

ic.disable()