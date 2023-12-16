# -*- coding: utf-8 -*-
# @File : 3.将二维数组变为一维数组.py
# @Author : 阿波
# @Time : 2023/9/1 11:14
# @Software: PyCharm

nums_2d=[[1,2,3],[4,5,6,7],[8,9]]
nums_1d=[]

# 第一种
for n in nums_2d:
    nums_1d.extend(n)
print(nums_1d)

# 第二种
# 这就是个两层for循环
nums_1d = [item for sublist in nums_2d for item in sublist]
print(nums_1d)

# 第三种
import functools
nums_2d = [[1,2,3],[4,5,6,7],[8,9]]
nums_1d = functools.reduce(lambda x, y: x + y, nums_2d)
print(nums_1d)




# 使用 reduce 方法计算列表中所有元素的和
numbers = [1, 2, 3, 4, 5]
sum = functools.reduce(lambda x, y: x + y, numbers)
print(sum)  # 输出：15




import operator
# 连接两个列表
list1= [1, 2, 3]
list2= [4, 5, 6]
result= operator.concat(list1, list2)
print(result)  # 输出：[1, 2, 3, 4, 5, 6]
# 连接两个字符串
string1= "Hello"
string2= "World"
result= operator.concat(string1, string2)
print(result)  # 输出：HelloWorld
# 在上述示例中，我们使用 operator.concat 方法将两个列表和两个字符串进行连接操作。
# 这个方法会返回一个新的序列对象，其中包含了连接后的元素。 需要注意的是，
# operator.concat 方法只能用于连接两个相同类型的序列对象，
# 例如两个列表或两个字符串。如果尝试连接不同类型的对象，将会引发错误。