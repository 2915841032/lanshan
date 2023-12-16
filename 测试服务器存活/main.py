# -*- coding: utf-8 -*-
# @File : main.py
# @Author : 阿波
# @Time : 2023/11/12 23:16
# @Software: PyCharm
import subprocess
import sys,os
import time
print(sys.argv)
cmd = "netstat -lntup|grep 0.0.0.0:%s|grep tcp|wc -l" % sys.argv[1]
startNginx='docker start nginx'

def runCmd(result):
    obj=subprocess.Popen(result, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    port = obj.stdout.read().decode('gbk').strip()

    return int(port)

def startCmd(port: int):
    '''默认启动Nginx'''
    if port == 0:
        print('服务未启动!!!')
        runCmd(startNginx)
        if int(runCmd(cmd)) == 0:
            print('启动失败!!!')
        else:
            print('启动成功')
    else:
        print('服务正常')

if __name__ == '__main__':
    port = int(runCmd(cmd))
    print(port)
    startCmd(port)