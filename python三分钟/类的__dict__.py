# -*- coding: utf-8 -*-
# @File : 类的__dict__.py
# @Author : 阿波
# @Time : 2023/9/10 13:57
# @Software: PyCharm
class Maiyou(object):
    a = 0
    b = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def normal_func(self):
        print('普通的函数')

    @staticmethod
    def static_func():
        print('静态函数')

    @classmethod
    def class_func(self):
        print('类函数')


if __name__ == '__main__':
    print('类的__dict__:')
    print(Maiyou.__dict__)
    print("="*30)

    obj = Maiyou('zhangsan', 18)
    print('对象的__dict__:')
print(obj.__dict__)

#
class Person:
    def __init__(self,_obj):
        self.name = _obj['name']
        self.age = _obj['age']
        self.energy = _obj['energy']
        self.gender = _obj['gender']
        self.email = _obj['email']
        self.phone = _obj['phone']
        self.country = _obj['country']
# 可以利用__dict__被简化成：
class Person:
    def __init__(self,_obj):
        self.__dict__.update(_obj)
data=Person(obj.__dict__)
print(data.__dict__)