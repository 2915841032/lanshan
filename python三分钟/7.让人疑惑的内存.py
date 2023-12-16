# -*- coding: utf-8 -*-
# @File : 7.让人疑惑的内存.py
# @Author : 阿波
# @Time : 2023/9/2 18:16
# @Software: PyCharm
a = 259
b = 259
print(a is b)


# is是比较两个对象在内存中地址是否相同
# ==是比较两个对象的值是否相同，它调用的是对象的__eq__方法

# class Student:
#     def __init__(self, name, no):
#         self.name = name
#         self.no = no  # 学号
#
#
# # 来测试一下is和 ==：
# s1 = Student('张三', '9527')
# s2 = Student('张三', '9527')
# print(id(s1))  # 打印s1的内存地址
# print(id(s2))  # 打印s2的内存地址
# print(s1 is s2)
# print(s1 == s2)


class Student:
    def __init__(self, name, no):
        self.name = name
        self.no = no  # 学号

    # 定义==函数，如果name和no都相同就认为是相等的
    def __eq__(self, other):
        return self.name == other.name and self.no == other.no


s1 = Student('张三', '9527')
s2 = Student('张三', '9527')
print(id(s1))
print(id(s2))
print(s1 == s2)
print(s1 is s2)
