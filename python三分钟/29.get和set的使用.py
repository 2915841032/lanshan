# -*- coding: utf-8 -*-
# @File : 29.get和set的使用.py
# @Author : 阿波
# @Time : 2023/9/7 23:48
# @Software: PyCharm
# class Maiyou():
#     def __init__(self, name, age, id_no):
#         self.name = name
#         self.age = age
#         self._id_no = id_no
#
#     def get_id_no(self):
#         return self._id_no
#
#     def set_id_no(self, id_no):
#         self._id_no = id_no
#
#
# m1 = Maiyou('Kevin', 18, '1234567890')
# print(m1.name)
# print(m1.age)
# print(m1.get_id_no())
# m1.set_id_no('66666666666')

# Descriptor，中文名字是描述器。它是一种特殊的类，它的作用是用来封装一个属性。它的特征就是需要有__get__和__set__函数
class IdDescriptor:
    def __get__(self, obj, objtype=None):
        value = obj._id_no
        print(f'获取age: {value}')
        return value

    def __set__(self, obj, value):
        obj._id_no = value
        print(f'age从{obj._id_no}更新为: {value}')


class Maiyou():
    id_no = IdDescriptor()

    def __init__(self, name, age, id_no):
        self.name = name
        self.age = age
        self.id_no = id_no


m1 = Maiyou('Kevin', 18, '1234567890')
m1.id_no
m1.id_no = '66666666666'

# m2 = Maiyou('Yushao', 16, '9876543210')
# m1.id_no
# m1.id_no = '888888888'
