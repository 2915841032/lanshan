# -*- coding: utf-8 -*-
# @File : 33.classmethod和staticmethod区别.py
# @Author : 阿波
# @Time : 2023/9/8 13:06
# @Software: PyCharm
class Circle:
    PI = 3.14159

    @classmethod
    def calculate_area(cls, radius):
        a = (radius ** 2) * cls.PI
        return a


ca = Circle.calculate_area(4)
print("面积是：", ca)


class Circle:

    @staticmethod
    def area(radius):  # 没有self关键字，但是需要传入参数
        a = (radius ** 2) * 3.14159
        return a


a = Circle.area(4)  # 无需实例化，直接从类里调
print("面积：", a)




class Circle:
    PI = 3.14159  # 类中的常量PI

    @classmethod
    def get_area(cls, radius):  # 类方法
        a = cls(radius).calculate()  # 调用实例函数得到面积值，cls(radius)可以理解成实例化
        return a

    def __init__(self, radius):  # 构造方法，传入半径值radius
        self.radius = radius

    def calculate(self):  # 实例方法，计算面积值a
        a = (self.radius ** 2) * self.PI
        return a


ca = Circle.get_area(4)
print("面积是：", ca)



