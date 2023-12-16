# -*- coding: utf-8 -*-
# @File : 39.定时运行.py
# @Author : 阿波
# @Time : 2023/8/31 13:40
# @Software: PyCharm

import schedule

# 假装是个爬虫任务
def job():
    print("正在爬取每日资讯。")
    return schedule.Callable

schedule.every(1).minutes.do(job)
# 每十分钟执行任务
schedule.every(10).minutes.do(job)

# 每个小时执行任务
schedule.every().hour.do(job)

# 每天的10:30执行任务
schedule.every().day.at("10:30").do(job)

# 每个月执行任务
schedule.every().monday.do(job)

# 每个星期三的13:15分执行任务
schedule.every().wednesday.at("13:15").do(job)

# 每分钟的第17秒执行任务
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()