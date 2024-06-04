# -*- coding: utf-8 -*-
# @File : 38.多继承.py
# @Author : 阿波
# @Time : 2023/9/6 12:34
# @Software: PyCharm
class mixin1:
    def method1(self):
        print('this is mixin method1')

    def method2(self):
        print('this is mixin method2')


class mixin2():
    def method3(self):
        print('this is mixin2 method3')

    def method4(self):
        print('this is mixin2 method4')


class Maishu(mixin1, mixin2):
    pass


ms = Maishu()
ms.method1()
ms.method2()
ms.method3()
ms.method4()
# ====================================================================================================
class RichDad:
    iq = 120
    money = 100_000_000

    def earn_money(self):
        print("赚钱！！")

    def hit(self):
        print("拿钱，揍儿子！")


class SmartDad:
    """
    这是一个docstring
    """
    iq = 160
    money = 1_000_000

    def make_atomic_bomb(self):
        print('造原子弹！')

    def hit(self):
        print("拿原子弹，轰儿子！")


class Son(RichDad,SmartDad):
    pass


# # 创造儿子
# son = Son()
# # 查看儿子IQ
# print(son.iq)
# # 查看儿子财产
# print(son.money)
#
# # 确认儿子是否能赚钱
# son.earn_money()
#
# # 确认儿子是否能造原子弹
# son.make_atomic_bomb()
#
# # 确认儿子喜欢用哪种方式揍人（调用多父类共有方法）
# son.hit()
print(SmartDad.__doc__)


# Python的MRO即Method Resolution Order（方法解析顺序），即在调用方法时，会对当前类以及所有的基类进行一个搜索，以确定该方法之所在，而这个搜索的顺序就是MRO。
# 这句话的意思就是，当儿子继承多爹属性或方法发生冲突时，以亲爹（继承位置）作优先选择，其次二爹，三爹...