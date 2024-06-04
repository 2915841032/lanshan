# -*- coding: utf-8 -*-
# @File : 23.日历制作.py
# @Author : 阿波
# @Time : 2023/9/4 19:25
# @Software: PyCharm
import calendar
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2023, 9)
print(str)


c = calendar.HTMLCalendar(calendar.MONDAY)
str = c.formatmonth(2022, 2)
print(str)
with open('日历.html','w',encoding='utf-8')as f:
    f.write(str)