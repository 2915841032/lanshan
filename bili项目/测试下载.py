# -*- coding: utf-8 -*-
# @File : 测试下载.py
# @Author : 阿波
# @Time : 2023/9/13 0:39
# @Software: PyCharm
import requests
headers = {
        'authority': 'www.bilibili.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://www.bilibili.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76',
    }
url="https://xy58x218x65x27xy.mcdn.bilivideo.cn:4483/upgcxcode/29/36/1265223629/1265223629-1-100113.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1694539382&gen=playurlv2&os=mcdn&oi=2936919974&trid=00004649f3b6636140c690cc927d8c0d0b17u&mid=88031177&platform=pc&upsig=ea77725beca54c99d79ae439a15f8a13&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=14002076&bvc=vod&nettype=0&orderid=0,3&buvid=47CF9962-FBA5-9D9F-9513-437C8F225A6789499infoc&build=0&f=u_0_0&agrr=0&bw=86306&logo=A0002000"
audio_url_content = requests.get(url=url, headers=headers).content
with open(f"4.mp4", mode='wb', ) as fp:
    fp.write(audio_url_content)
print('ok')