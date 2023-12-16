# -*- coding: utf-8 -*-
# @File : 20.可变对象,不可变对象.py
# @Author : 阿波
# @Time : 2023/9/3 20:44
# @Software: PyCharm
name = '麦叔'
print(id(name))
name = '麦叔2'
print(id(name))


def func1():
    name = '张三'
    print('func1: {}'.format(name))
    func2(name)
    print('func1: {}'.format(name))


def func2(name):
    print('func2: {}'.format(name))
    name = '李四'
    print('func2: {}'.format(name))

func1()

# 	我们来看一下过程：
# 	• func1中定义的name是张三
# 	• 然后func1把name传给了func2
# 	• 虽然func2中把name修改成了李四
# 	• 但func1中的name仍然是张三
# 	这是因为func1给func2传递的是指向对象”张三“的引用。
# 	当func2把name修改为”李四“的时候，因为字符串是immutable的，所以”李四“是一个新的对象。
# 	所以这时候func2指向了新对象”李四“，而func1还是指向老的对象”张三“，所以这个改变不会影响func1中的后续打印结果。
# 	这样看起来好像Python是传递了一个值过去，但实际上Python传递的是引用。但由于字符串是immutable的，它不可能改变func1中的值。