# -*- coding: utf-8 -*-
# @File : 捕获5.py
# @Author : 阿波
# @Time : 2023/9/12 21:18
# @Software: PyCharm
import cv2

# 创建VideoCapture对象来调用摄像头
cap = cv2.VideoCapture(0)

# 定义视频编码器
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 创建VideoWriter对象，用于将视频帧写入文件
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# 设置计时器，用于记录捕获的时间
timer = 0

while True:
    # 读取摄像头捕捉到的图像
    ret, frame = cap.read()

    # 将图像写入视频文件
    out.write(frame)

    # 显示图像
    cv2.imshow('Camera', frame)

    # 计时器自增
    timer += 1

    # 捕获5秒后退出循环
    if timer == 100:
        break

    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放VideoCapture和VideoWriter对象
cap.release()
out.release()

# 关闭窗口
cv2.destroyAllWindows()