# -*- coding: utf-8 -*-
# @File : 12.python执行其他文件.py
# @Author : 阿波
# @Time : 2023/9/2 18:54
# @Software: PyCharm
import subprocess

result = subprocess.run(["ping", "baidu.com"], capture_output=True, text=True)

print(result.returncode)  # 子进程返回码
print(result.stdout)  # 子进程标准输出
print(result.stderr)  # 子进程标准错误输出