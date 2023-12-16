# -*- coding: utf-8 -*-
# @File : 42.扩展内置类.py
# @Author : 阿波
# @Time : 2023/9/5 22:35
# @Software: PyCharm
def find(elements, keyword):
    return [x for x in elements if keyword in x]

names = ['麦叔', '麦子', '周五好', '不麦', '周末好', '核酸检测了吗？']

result = find(names, '麦')
print(result)


class mailist(list):
    def find(self, keyword):
        return [x for x in self if keyword in x]


names = mailist()
names.extend(['麦叔', '麦子', '周五好', '不麦', '周末好', '孙子', '核酸检测了吗？', '不要啊'])

print(names.find('麦'))
print(names.find('子'))
print(names.find('不'))
