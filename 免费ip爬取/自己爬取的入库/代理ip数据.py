# encoding=utf-8
import csv
import time
from multiprocessing.pool import ThreadPool

import requests
import pandas as pd


baseurl = "http://www.66ip.cn/"
df_list = []
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Cookie": "Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1679758826; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1679759213",
    "Referer": "http://www.66ip.cn/10.html",
    "Host": "www.66ip.cn"
}
for i2 in range(1,5):
    url2 = baseurl + str(i2) +".html"
    html = requests.get(url2,headers=header)
    html.encoding='gbk'
    df = pd.read_html(html.text)[-1]
    df.columns = df.head(1).values[0]
    df.drop(index=0, inplace=True, axis=0)
    df_list.append(df)
    time.sleep(1)
    print("成功爬取一页")
dfs = pd.concat(df_list)
dfs.reset_index(inplace=True)
dfs.drop('index', axis=1, inplace=True)
dfs.to_csv(f"ip数据.csv", index=False)

alive_ip = []

def validate(ip):
    IP = {'http': ip}  # 指定对应的 IP 进行访问网址
    try:
        r = requests.get('https://www.bilibili.com/', proxies=IP,
                         timeout=3)  # proxies 设定对应的代理 IP 进行访问， timeout 设定相应的时间之后停止等待响应
        if r.status_code == 200:
            print("成功:{}".format(ip))
            alive_ip.append(ip)  # 有效的 IP 则添加进去
    except:
        print("无效")

df=pd.read_csv('ip数据.csv')

df['ok']=df['ip']+':'+df["端口号"].astype(str)
print(df.shape[0])
# print(list(df['ok']))

pool = ThreadPool(20)  # 多线程 设置并发数量！
pool.map(validate, list(df['ok']))  # 用 map 简捷实现 Python 程序并行化
csv_file = open('ip数据2.csv', 'w', newline='')
writer = csv.writer(csv_file)
for ip in alive_ip:
    writer.writerow([ip])
    print(ip)
print("成功保存所有有效 ip ")