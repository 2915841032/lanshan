# -*- coding: utf-8 -*-
# @File : 29.python的__getattribute__.py
# @Author : 阿波
# @Time : 2023/9/7 1:02
# @Software: PyCharm
#  Python解释器首先访问__getattribute__函数去找name属性。看这个这个函数的名字：「get attribute」，顾名思义，就是获得属性的意思。
# 如果在上一步找不到name属性，解释器会去执行__getattr__函数。相当于候补队员。
class Maiyou():
    def __init__(self, name, age, id_no):
        self.name = name
        self.age = age
        self.id_no = id_no  # 深证号码

    def __getattribute__(self, item):
        """所有以id开头的属性都不能直接访问"""
        if item.startswith('id'):
            return '隐私属性，不能直接访问'
        return object.__getattribute__(self, item)


m1 = Maiyou('Kevin', 18, '1234567890')
print(m1.name)
print(m1.age)

# 这一行拦截访问！
print(m1.id_no)