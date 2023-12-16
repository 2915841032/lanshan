# -*- coding: utf-8 -*-
# @File : 测试.py
# @Author : 阿波
# @Time : 2023/9/5 23:16
# @Software: PyCharm

import tkinter as tk
import tkinter.messagebox
import random
import threading
import time

def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.geometry("200x100" + "+" + str(a) + '+' + str(b))

    def show_message():
        tkinter.messagebox.showwarning('Windows警告', '你的电脑正在被攻击！')

    while True:
        x = window.winfo_x()
        y = window.winfo_y()
        for i in range(10):
            window.geometry("200x100" + "+" + str(a+random.randint(-10, 10)) + '+' + str(b+random.randint(-10, 10)))
            window.update()
            time.sleep(9)

        window.after(1000, show_message)
        window.mainloop()

# 创建线程
threads = []
for i in range(2):
    t = threading.Thread(target=boom)
    threads.append(t)
    threads[i].start()

# 进入主循环
tk.mainloop()