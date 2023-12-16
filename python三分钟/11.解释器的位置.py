# -*- coding: utf-8 -*-
# @File : 11.解释器的位置.py
# @Author : 阿波
# @Time : 2023/9/2 18:34
# @Software: PyCharm
import os
import sys
# python_path = os.path.dirname(sys.executable)
python_path=os.path.dirname(sys.executable)
print(python_path)
print(list(sys.path))
