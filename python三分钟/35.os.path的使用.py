# -*- coding: utf-8 -*-
# @File : 35.os.path的使用.py
# @Author : 阿波
# @Time : 2023/9/5 12:33
# @Software: PyCharm
import os
#环境变量打印
# for key, value in os.environ.items():
#     print(f"{key}: {value}")
APPDATA='$APPDATA\\1.txt'
print(os.path.expanduser(r'C:\Users\lan\佘老师的作业'))#把path中包含的"~"和"~user"转换成用户目录
print(os.path.expandvars(APPDATA))  #根据环境变量的值替换path中包含的"和{name}"
print(os.path.getatime(r'C:\Users\lan\佘老师的作业\爬虫.docx'))#返回最近访问时间（浮点型秒数）
print(os.path.getmtime(r'C:\Users\lan\佘老师的作业\爬虫.docx'))#返回文件修改的时间
print(os.path.getctime(r'C:\Users\lan\佘老师的作业\爬虫.docx'))#返回创建的时间
print(os.path.getsize(r'C:\Users\lan\佘老师的作业\爬虫.docx'))#返回文件的大小
print(os.path.isabs(r'C:\Users\lan\佘老师的作业\爬虫.docx'))#判断是否为绝对路径
print(os.path.isfile(r'C:\Users\lan\佘老师的作业\爬虫.docx'))#判断路径是否为文件
path = os.path.join('dir1', 'dir2', 'file.txt'); print(path)#把目录和文件名合成一个路径
print(os.path.split(r'C:\Users\lan\佘老师的作业\爬虫.docx'))#把路径分割成 dirname 和 basename，返回一个元组
print(os.path.splitdrive(r'C:\Users\lan\佘老师的作业\爬虫.docx'))#一般用在 windows 下，返回驱动器名和路径组成的元组
print(os.path.splitext(r'C:\Users\lan\佘老师的作业\爬虫.docx'))#分割路径，返回路径名和文件扩展名的元组

# current_dir = os.path.dirname(os.path.abspath(__'file__))
# current_dir = os.path.split(__file__)
# print(current_dir)



v= os.remove(r'E:\pycharm_Community_version_project\测试\1爬取ip网的地址.py')
print(v)

