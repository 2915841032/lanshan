# -*- coding: utf-8 -*-
# @File : 40.实现类.py
# @Author : 阿波
# @Time : 2023/8/2 10:16
# @Software: PyCharm
# 10岁的小明步行走到上海火车站。
# 把上面这句话写成代码，你会怎么写？
import time


class pelpeo():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def run(self, decition):
        print(f'{self.name}步行去{decition}')
        time.sleep(2)
        print(f'{self.name}步行到了{decition}')


xiaoming = pelpeo('小明', 18, "男")
xiaoming.run("北京")



s = lambda x,y : x**2 + y**2

array1 = [1,3,5,7,9]
array2 = [2,4,6,8,10]

print(list(map(s, array1, array2)))