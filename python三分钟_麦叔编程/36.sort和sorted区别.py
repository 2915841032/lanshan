# -*- coding: utf-8 -*-
# @File : 36.sort和sorted区别.py
# @Author : 阿波
# @Time : 2023/9/4 19:35
# @Software: PyCharm

# sort() 在原列表上直接原地排序，会改变原列表。
# sorted() 会创建一个新的列表，不会改变原列表。

foods = ['milk', 'bread', 'tea']
print('foods: {}'.format(foods))
foods.sort(reverse=False)
print('foods: {}'.format(foods))
print(dir(list))


foods = ['milk', 'bread', 'tea']
new_foods = sorted(foods)
print('foods: {}'.format(foods))
print('new_foods: {}'.format(new_foods))