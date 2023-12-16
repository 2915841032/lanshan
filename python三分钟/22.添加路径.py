# -*- coding: utf-8 -*-
# @File : 22.添加路径.py
# @Author : 阿波
# @Time : 2023/9/4 18:16
# @Software: PyCharm

import sys
import os

# 获取当前文件的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取模块文件的绝对路径
module_dir = os.path.join('E:\pycharm_Community_version_project\[置顶]爬虫\爬取视频\\')

# 将模块文件所在的目录添加到搜索路径中
sys.path.append(module_dir)
print(sys.path)

# 导入模块文件中的类对象
import class_main_1
# 使用导入的类对象
obj = class_main_1.MovieMerger()
print(obj)
# obj.run()