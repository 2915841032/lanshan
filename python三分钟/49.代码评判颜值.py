# -*- coding: utf-8 -*-
# @File : 49.代码评判颜值.py
# @Author : 阿波
# @Time : 2023/9/10 14:44
# @Software: PyCharm
import ybc_face
import ybc_box
from PIL import Image

pic = ybc_box.fileopenbox()
res = ybc_face.info(pic)
box.msgbox(f'请告诉我，我的颜值：{res}, {pic}。')