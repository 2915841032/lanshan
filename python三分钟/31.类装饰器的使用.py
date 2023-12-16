# -*- coding: utf-8 -*-
# @File : 31.类装饰器的使用.py
# @Author : 阿波
# @Time : 2023/9/8 12:16
# @Software: PyCharm
class Circle:

    def __init__(self, dia):
        self.dia = dia

    @property
    def area(self):
        a = (self.dia ** 2) * 3.14
        return a


c = Circle(4)
print("面积：", c.area)  # 这里的area方法可以不用带（）了


# @staticmethod
# 上文算面积的方式有点麻烦，还要实例化类。能不能有一种即调即用的方式？
# 那就可以拿出 @ staticmethod装饰器，「带上这个装饰器的方法可以不实例化就能用」。
# 因为不需要将类实例化就能调用，所以构造方法中的实例属性都是不能拿来用的，所以参数里也没有self关键字。
#
class Circle:

    @staticmethod
    def area(dia):  # 没有self关键字，但是需要传入参数
        a = (dia ** 2) * 3.14
        return a


a = Circle.area(4)  # 无需实例化，直接从类里调
print("面积：", a)



