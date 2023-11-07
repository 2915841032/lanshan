# -*- coding: utf-8 -*-
# @File : 测试1.py
# @Author : 阿波
# @Time : 2023/9/12 18:10
# @Software: PyCharm
import cv2

# 打开摄像头
cap = cv2.VideoCapture(0)  # 0代表默认摄像头，如果有多个摄像头，可以尝试修改参数来选择不同的摄像头
while True:
    # 读取摄像头视频帧
    ret, frame = cap.read()
    # 在窗口中显示视频帧
    cv2.imshow('Camera', frame)
    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()

# 关闭窗口
cv2.destroyAllWindows()