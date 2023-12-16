# -*- coding: utf-8 -*-
# @File : 5.一条语句合并两个字典.py
# @Author : 阿波
# @Time : 2023/9/2 16:04
# @Software: PyCharm
a = {'zhangsan': 99, 'lisi': 88, 'maisu': 77}
b = {'wangwu': 89, 'zhaoliu': 97}

# 第一种
c={**a,**b}
print(c)

# 第二种
a.update(b)  # 把b中的键值对放入到a中去，如果a和b有相同的键值对，就用b中的值更新a。
print(a)  # 结果是：{'zhangsan':99, 'lisi':88, 'maisu':77, 'wangwu':89, 'zhaoliu:97'}


# 如果a和b中都有zhangsan这个key怎么办？
# 前面的例子已经给出了答案：会保留后面一个字典中的值。这个规则同时适用于update和或运算符。
