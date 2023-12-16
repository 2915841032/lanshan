# -*- coding: utf-8 -*-
# @File : 21.可变参数和可变关键词参数.py
# @Author : 阿波
# @Time : 2023/9/4 11:01
# @Software: PyCharm
def add2(a, b, *more):
    print(type(more))  # 打印一下more的类型
    sum = a + b
    for i in more:
        sum = sum + i
    print(sum)
add2(2,12,45,78)


def add(a,b,**others):
    print(type(others))
    sum=a+b
    print(others)
add(12,45,lk="王五",lank="张三")