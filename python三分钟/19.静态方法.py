# -*- coding: utf-8 -*-
# @File : 19.静态方法.py
# @Author : 阿波
# @Time : 2023/9/3 20:26
# @Software: PyCharm

# @staticmethod是Python中的一个装饰器（Decorator），
# 用于定义静态方法。静态方法是一种在类中定义的方法，
# 不需要访问实例的属性或方法，也不需要实例化类对象即可调用。
# 静态方法与类对象无关，因此它们不需要传递self参数。
# 使用@staticmethod装饰器可以将一个普通的函数转换为静态方法。
# 静态方法可以通过类名直接调用，而不需要创建类的实例。
# 在静态方法中，无法访问类的实例变量，只能访问类的静态变量。

class MyClass:
    static_var = 10

    @staticmethod
    def static_method():
        print("This is a static method")
        print("Static variable:", MyClass.static_var)


# 调用静态方法
MyClass.static_method()

# 通过@staticmethod装饰器，我们将普通函数 static_method 转换为静态方法。
# 在静态方法中，我们可以访问类的静态变量 static_var ，并且可以通过类名直接调用静态方法 MyClass.static_method() 。
# =======================================================================================================================================
class Duck:

    def duck_walk(self):
        print('走🦆步')

    def duck_sound(self):
        print('嘎嘎嘎')


# 全聚德
class QuanJude:

    @staticmethod
    def cook(duck):
        print("-- 鸭子来了，先检查一下 ---")
        # 走走看
        duck.duck_walk()
        # 叫两声听听
        duck.duck_sound()

        print("验证完毕，可以下锅了")


# 搞两只鸭子
d1 = Duck()
d2 = Duck()

# 送到全聚德
# QuanJude.cook(d1)
# QuanJude.cook(d1)
# ========================================================================================================
class StudentScore:
    chinese_pass_score = 52  # 及格线
    math_pass_score = 52  # 及格线
    english_pass_score = 52  # 及格线

    # 计算总的及格分数，和单个实例无关，但是和各科及格线有关
    @classmethod
    def total_pass_score(cls):
        return cls.english_pass_score + cls.chinese_pass_score + cls.math_pass_score

    def __init__(self, chinese, math, english):
        self.chinese = chinese
        self.math = math
        self.english = english

    # 计算总成绩，和实例有关
    def total(self):
        return self.chinese + self.math+self.english

    # 计算平均成绩，和实例有关
    def avg(self):
        return self.total() / 3

    # 这个静态方法不需要访问实例属性，也不需要访问类的全局变量
    @staticmethod
    def introduction():
        print('这里想不出很好的例子.... 参考全聚德的例子')
dfa=StudentScore(120,100,100)
print(dfa.total_pass_score())