# -*- coding: utf-8 -*-
# @File : 29.getattr.py
# @Author : 阿波
# @Time : 2023/9/6 23:25
# @Software: PyCharm
class Maiyou():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __getattr__(self, item):
        self.__dict__[item] = '不知道'
        return self.__dict__[item]

m1 = Maiyou('Kevin', 18)
print(m1.name)
print(m1.age)
print(m1.gender)
