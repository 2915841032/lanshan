# -*- coding: utf-8 -*-
# @File : 34.python的swith.py
# @Author : 阿波
# @Time : 2023/9/8 17:14
# @Software: PyCharm
def fake_swith_2(grade: str) -> str:
    level = {
        "A": "优秀",
        "B": "良好",
        "C": "良好",
        "D": "及格",
        "F": "你需要再努力努力",
    }
    try:
        g = level[grade]
    except Exception:
        g = "未知等级"
    return g


print(fake_swith_2('A'))
