# -*- coding: utf-8 -*-
# @File : 18.合并csv文件.py
# @Author : 阿波
# @Time : 2023/9/3 15:02
# @Software: PyCharm
import os

import pandas as pd

# 定义一个空列表,全局变量
file_list = []


# 查找符合要求的文件
def search_file(path):
    # 切换当前目录为指定路径
    os.chdir(path)
    # 定义需要查找的文件类型
    search_list = ['.csv']
    # 列举当前目录下的文件名
    allFile = os.listdir(path)
    # 遍历所有文件名
    for i in allFile:
        # 用于分离文件名和扩展名，返回（name,extension)元组，此处只返回扩展名
        extension = os.path.splitext(i)[1]
        if extension in search_list:
            # getcwd()获取当前工作目录；sep输出文件的路径分隔符；linesep是换行
            file_list.append(os.getcwd() + '\\' + i)
        # 判断指定路径i存在并且是一个目录
        elif os.path.isdir(i):
            # 递归调用
            search_file(i)
            # 递归调用后返回上一层目录
            os.chdir(os.path.dirname(path))


# 把运行结果文件保存至本地磁盘 “/root/Desktop/home/数据处理结果/” 目录中
def save_file(file_list):
    # 指定文件存放位置
    dir_name = r'E:\pycharm_Community_version_project\python三分钟\\'
    # 判断是否存在该路径
    if not os.path.isdir(dir_name):
        # 如果目录不存在则创建
        os.mkdir(dir_name)
    # open函数将内容写入指定目录txt下
    f = open(dir_name + 'file_list.txt', 'w', encoding='utf-8')
    # 将列表中的内容写入文件中
    f.writelines(file_list)
    # 关闭文件
    f.close()
    print(f'查找完成，文件已保存至本地磁盘 {dir_name} 目录中')


def count_csv(file_list):
    print(file_list)
    csvdata = []
    for i in (file_list):
        csv = pd.read_csv(i)
        csvdata.append(csv)
    dfs = pd.concat(csvdata, axis=0)
    dfs.to_csv("restult.csv", index=False)
    pass


# 主函数
if __name__ == '__main__':
    path = input('请输入开始搜索的目录：')
    # 判断输入的搜索目录是否存在
    while not path:
        print('搜索目录不存在！')
        path = input('请输入开始搜索的目录：')
    search_file(path)
    save_file(file_list)
    count_csv(file_list)
