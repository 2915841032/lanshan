# -*- coding: utf-8 -*-
# @File : 13.yield的使用.py
# @Author : 阿波
# @Time : 2023/9/2 19:40
# @Software: PyCharm


# return
# def waimai(name):
#     print('cooking ' + name)
#     print('............')
#     print('此处省略2022行做饭的语句')
#     print('............')
#     return f'美味的{name}好了'
#
#
# print(waimai('蛋炒饭'))
# print(waimai('胡辣汤'))

# yield的使用
def have_some_wine():
    print('先开一瓶酒，共有700毫升')
    wine = 700
    while wine > 0:
        # 取酒
        if wine > 200:
            get_wine = 200
            wine = wine - 200
        else:
            get_wine = wine
            wine = 0

        # 把酒送给客人
        print('您的酒来了：200毫升')

    yield get_wine

    # 开一瓶酒


mywine = have_some_wine()

# 可以多次来喝，直到喝光为止
for i in mywine:
    print(f'我今天喝{i}毫升')
