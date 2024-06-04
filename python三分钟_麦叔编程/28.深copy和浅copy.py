# -*- coding: utf-8 -*-
# @File : 28.深copy和浅copy.py
# @Author : 阿波
# @Time : 2023/9/5 20:53
# @Software: PyCharm
import copy

class Coder:

    def __init__(self, nickname, experience_years, skills):
        self.nickname = nickname
        self.experience_years = experience_years
        self.skills = skills

maishu = Coder('maishu', 15,['Java', 'Ruby', 'Python', 'Shell', 'Swift', 'Objective-C', 'Flutter', 'JavaScript', 'R', 'C', 'C++'])

guishu = copy.copy(maishu)

print(f'龟叔的名字是：{guishu.nickname}')

guishu.nickname = '龟叔'

print(f'麦叔的名字是：{maishu.nickname}')

print(f'龟叔的名字是：{guishu.nickname}')

guishu.skills.append('易语言')

print(f'麦叔的技能是：{maishu.skills}')

print(f'龟叔的技能是：{guishu.skills}')
# ===========================================================================
import copy


# class Coder:
#
#     def __init__(self, nickname, experience_years, skills):
#         self.nickname = nickname
#         self.experience_years = experience_years
#         self.skills = skills


maishu = Coder('maishu', 15,
               ['Java', 'Ruby', 'Python', 'Shell', 'Swift', 'Objective-C', 'Flutter', 'JavaScript', 'R', 'C', 'C++'])

guishu = copy.deepcopy(maishu)  # 唯一改动

print(f'龟叔的名字是：{guishu.nickname}')

guishu.nickname = '龟叔'

print(f'麦叔的名字是：{maishu.nickname}')

print(f'龟叔的名字是：{guishu.nickname}')

guishu.skills.append('易语言')

print(f'麦叔的技能是：{maishu.skills}')

print(f'龟叔的技能是：{guishu.skills}')
