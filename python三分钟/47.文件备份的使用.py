# -*- coding: utf-8 -*-
# @File : 47.文件备份的使用.py
# @Author : 阿波
# @Time : 2023/9/9 23:41
# @Software: PyCharm
from os import rename

with open('maishu20220427.txt', 'w') as f:
    f.write("ok")
# 写入文件的代码逻辑
# 写入时间约一分钟

# 把原来的文件备份一下
rename('backup_maishu.txt', 'maishu20220427.txt')

# 把新文件重命名成主文件
rename('maishu20220427.txt', 'backup_maishu.txt')

# 删除最老的一份备份，只保留最新的5份
import os
import glob

def delete_backup(keep):
    backup_files = glob.glob("backup_*.txt")  # 假设备份文件名以 "backup_" 开头并以 ".txt" 结尾
    backup_files.sort(key=os.path.getmtime, reverse=True)  # 按修改时间逆序排序备份文件列表
    if len(backup_files) <= keep:
        print("没有需要删除的备份文件。")
        return
    files_to_delete = backup_files[keep:]
    for file in files_to_delete:
        os.remove(file)
        print(f"已删除备份文件: {file}")

# 调用函数，保留最新的5个备份
delete_backup(keep=5)