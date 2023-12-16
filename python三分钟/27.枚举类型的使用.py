# -*- coding: utf-8 -*-
# @File : 27.枚举类型的使用.py
# @Author : 阿波
# @Time : 2023/9/5 18:59
# @Software: PyCharm
class Gender:
    MAN = 0
    WOMAN = 1
    BOTH = 2


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


tom = Person('Tom', Gender.MAN)
mike = Person('Tom', Gender.MAN)