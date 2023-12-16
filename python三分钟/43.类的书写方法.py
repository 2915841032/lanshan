# -*- coding: utf-8 -*-
# @File : 43.类的书写方法.py
# @Author : 阿波
# @Time : 2023/9/8 17:29
# @Software: PyCharm
# 	说说规范
# 	1. 缩进一致
# 	2. 方法之间，方法与类变量间，需要一个空行分隔。
# 	3. 如果存在多个相同种类的方法，请把相关（有互相调用）方法放在一起（或前或后）
# 	4. 一个项目内的类结构尽可能一致，
# 	5. 如果项目没有此类规范，请参考以下结构顺序
# 	❝
# 	6. 类变量
# 	7. 构造方法__init__
# 	8. 内置特殊方法__call，__repr__
# 	9. 类方法
# 	10. 静态方法
# 	11. 属性
# 	12. 实例方法
# 私有方法 ——— 摘自《Python代码整洁之道》
import random


class Animal:
    count = 0
    colors = ['黑', '白', '花']

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwagrs):
        cls.born()
        return object.__new__(cls)

    def __str__(self):
        return "我是：" + self.name

    @classmethod
    def born(cls):
        cls.count += 1

    @staticmethod
    def dig():
        print('我在寻宝。')

    @property
    def color(self):
        return random.choice(self.colors)

    def eat(self, food):
        print('我最喜欢吃：' + food)
