# -*- coding: utf-8 -*-
# @File : 1.全局变量在函数中的使用.py
# @Author : 阿波
# @Time : 2023/8/31 22:03
# @Software: PyCharm
count=99
def quguan():
    global count
    count = count - 1
    print('lank的粉丝数是{}'.format(count))
quguan()