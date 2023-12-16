# -*- coding: utf-8 -*-
# @File : 48.return表达式，finally语句块，return操作的顺序.py
# @Author : 阿波
# @Time : 2023/9/10 14:19
# @Software: PyCharm
# 	return语句包含两部分，一部分return关键字后的表达式，比如number_list.append('return')，另一部分是return本身，也就是退出函数的操作。
# 	所以正确的顺序是：
# return表达式，finally语句块，return操作
def play_numer():
    number_list = []
    while True:
        print('-----------------')
        try:
            number = input('输入一个数字：')
            print(int(number) / 2)
            if number == '886':
                return number_list.append('return')
        except Exception as e:
            print(f'出错了：{e}')
        finally:
            number_list.append(number)
            print(number_list)


play_numer()

#