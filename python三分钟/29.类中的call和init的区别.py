# -*- coding: utf-8 -*-
# @File : 29.类中的call和init的区别.py
# @Author : 阿波
# @Time : 2023/9/6 18:43
# @Software: PyCharm
class Person:
    def __init__(self):
        print("init")

    def __call__(self):
        print("call")


m1 = Person()
m1()
m1()
m1()
# __init__是对象的构造函数，用类（Person）来创建一个新实例的时候会调用一次，仅仅一次。
# __call__会让对象实例变成一个可以被调用的对象，可以直接通过对象名()的方式调用。所以例子中我们可以写m1()。它其实就是一个普通的魔术函数，你想在里面做什么就做什么。