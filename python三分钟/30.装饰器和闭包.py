# -*- coding: utf-8 -*-
# @File : 30.装饰器和闭包.py
# @Author : 阿波
# @Time : 2023/9/6 22:57
# @Software: PyCharm
class WashHandDecorator(object):
    def __init__(self, f):
        self.f = f
        print("洗手装饰器组装中...")

    def __call__(self):
        print("先洗手，再做饭...")
        self.f()
    pass


@WashHandDecorator
def cook():
    print("做饭中😊...美味香喷喷😄...但是自己不能吃😭...")


# cook()

# 无实参
class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 在函数执行前的装饰逻辑
        print("Decorator logic before function execution")
        result = self.func(*args, **kwargs)
        # 在函数执行后的装饰逻辑
        print("Decorator logic after function execution")
        return result

@Decorator
def my_function():
    print("Hello, world!")

# my_function()


# 有实参
class Decorator:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            # 在函数执行前的装饰逻辑
            print(f"Decorator arguments: {self.arg1}, {self.arg2}")
            result = func(*args, **kwargs)
            # 在函数执行后的装饰逻辑
            print("函数执行完毕")
            return result
        return wrapped_func

@Decorator("arg1_value", "arg2_value")
def my_function():
    print("Hello, world!")

my_function()

def decorator1(func):
    def wrapper():
        print("Decorator 1 - Before function execution")
        func()
        print("Decorator 1 - After function execution")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 - Before function execution")
        func()
        print("Decorator 2 - After function execution")
    return wrapper

@decorator1
@decorator2
def my_function():
    print("Hello, world!")

my_function()