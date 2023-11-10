import datetime
import time


# cday = datetime.strptime('2017-2-6 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday, type(cday))

def getYesterday():
   # 获取昨天日期的字符串格式的函数
   #获取今天的日期
   today = datetime.date.today()
   print(today)
   #获取一天的日期格式数据
   oneday = datetime.timedelta(days=1)
   #昨天等于今天减去一天
   yesterday = today - oneday
   #获取昨天日期的格式化字符串
   yesterdaystr = yesterday.strftime('%Y-%m-%d')
   #返回昨天的字符串
   return yesterdaystr


# 获取当前时间
print(datetime.datetime.now())

# 获取当前日期
print(datetime.date.today())

# 获取离某一个节日的时间差

chrismas_day_gap = datetime.datetime(2024, 12, 25, 0, 0, 0) - datetime.datetime.now()  # 具体时间
chrismas_day_date = datetime.date(2023, 12, 25) - datetime.date.today()  # 只有日期
print(chrismas_day_gap)
print(chrismas_day_date)

# 计算当天日期,前后的100天(加减就行)
d3=datetime.datetime(2021,2,7)
print(d3+datetime.timedelta(days=100))
print(datetime.date.today()+datetime.timedelta(days=100))

# 计算时间差
today = datetime.date.today()
other_date = datetime.date(2021, 9, 1)  # 假设你要计算的日期是 2021 年 9 月 1 日
delta = today - other_date
print(delta)  # 输出为：14 days, 0:00:00