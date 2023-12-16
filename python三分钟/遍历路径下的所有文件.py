# -*- coding: utf-8 -*-
# @File : 遍历路径下的所有文件.py
# @Author : 阿波
# @Time : 2023/9/5 14:12
# @Software: PyCharm
import os

def visit_func(dirpath, dirnames, filenames):
    # dirpath: 当前遍历的文件夹路径
    # dirnames: 当前文件夹下的所有子文件夹名称列表
    # filenames: 当前文件夹下的所有文件名称列表

    # 在这里可以对文件夹和文件进行操作
    for dirname in dirnames:
        print("子文件夹:", os.path.join(dirpath, dirname))
    for filename in filenames:
        print("文件:", os.path.join(dirpath, filename))

# 使用os.walk()遍历路径
path = "E:\pycharm_Community_version_project\python三分钟"
print(os.walk(path))
for dirpath, dirnames, filenames in os.walk(path):
    visit_func(dirpath, dirnames, filenames)
