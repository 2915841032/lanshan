# encoding=utf-8
import time
import requests
import pandas as pd
from sqlalchemy import create_engine
# import pymysql
# db = pymysql.Connect(user='root', password='root', host="localhost", database="代理ip", port=3306, charset="utf8")
# cursor = db.cursor()
# commit = db.commit()
# baseurl = "http://www.66ip.cn/"
# connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)
connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}'.format('root', 'root', 'localhost', 3306, '代理ip')
engine=create_engine(connect_info)

baseurl = "https://www.kuaidaili.com/free/inha/"
df_list = []
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'channelid=0; sid=1683168789332145; _gcl_au=1.1.995287009.1683168794; _ga=GA1.2.2031901164.1683168794; _gid=GA1.2.1394547886.1683168794; _gat=1; Hm_lvt_e0cc8b6627fae1b9867ddfe65b85c079=1683168794; Hm_lpvt_e0cc8b6627fae1b9867ddfe65b85c079=1683168794',
    'Host': 'www.kuaidaili.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.0.0',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
for i2 in range(1, 5):
    url2 = baseurl + str(i2) + "/"
    print(url2)
    html = requests.get(url2, headers=header)
    html.encoding = 'utf-8'
    df = pd.read_html(html.text)[-1]
    print(df)
    df_list.append(df)
    time.sleep(1)
    print("成功爬取一页")
dfs = pd.concat(df_list,axis=0)
dfs.reset_index(inplace=True)
dfs.drop('index', axis=1, inplace=True)
print(dfs)

dfs.to_sql(name = '代理ip', con = engine, index = False, if_exists = 'append')
dfs.to_csv(f"ip数据2.csv", index=False)
print("写入文件ok")