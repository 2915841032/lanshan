# -*- coding: utf-8 -*-
# @File : 26.序列的列表.py
# @Author : 阿波
# @Time : 2023/9/5 11:50
# @Software: PyCharm


# 1.使用方括号创建列表
names = ['张三', '李四', '王五', 94, 83.5]
print(names)


# 2.构造方法: 使用列表的构造方法list()也可以创建一个空的列表。
scores = list()
print(scores)
# 3.类型转换：使用构造方法也可以把其他类型的数据转换成列表：

# 创建1个范围,把范围转换成列表
r = range(1, 100)
nums = list(r)
print(nums)


scores.append('兰蔻')
scores.insert(0,"婪")
scores.extend("oi")
print(scores)

del scores[0]
scores.pop(1)
scores.remove('i')
print(scores)


names = ['tom', 'mike', 'tom', 'jerry', 'tom']
if 'tommy' not in names:
    names.append('tommy')
else:
    print(names.index('tommy'))