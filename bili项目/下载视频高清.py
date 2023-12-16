# -*- coding: utf-8 -*-
# @File : 下载视频.py
# @Author : 阿波
# @Time : 2023/8/16 10:24
# @Software: PyCharm
import json
import os
import re

import requests
from bs4 import BeautifulSoup
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip


url = ('https://www.bilibili.com/video/BV15m4y117D1/?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click&vd_source=bff9605a6957493576220a2ca2264731')
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
data = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(data, 'lxml')
title = soup.select('title')[0].get_text()
vb = re.compile("[\u4e00-\u9fa5A-Za-z0-9]")
title1 = re.findall(vb, ''.join(title))
c = ''.join(title1)
print(c)
data_1 = soup.select('script')[3].get_text()
result_data = data_1.split('=', 1)[1]
v1 = json.loads(result_data)


audio_url = v1['data']['dash']['video'][0]['baseUrl']
vieio_url = v1['data']['dash']['audio'][0]['baseUrl']

audio_url_content = requests.get(url=audio_url, headers=headers).content
vie_url_content = requests.get(url=vieio_url, headers=headers).content

os.chdir(os.getcwd())
# 判断是否存在该路径
dir_name = os.getcwd() + '\下载'
if os.path.isdir(dir_name):
    pass
else:
    # 如果目录不存在则创建
    os.mkdir(dir_name)

with open(f"{dir_name}\\{c}.mp4", mode='wb', ) as fp:
    fp.write(audio_url_content)

with open(f"{dir_name}\\{c}.mp3", mode='wb', ) as fp:
    fp.write(vie_url_content)
#

video = VideoFileClip(f'{dir_name}\\{c}.mp4')
audio = AudioFileClip(f'{dir_name}\\{c}.mp3')
video_merge = video.set_audio(audio)
video_merge.write_videofile(f"{dir_name}\\{c}结果.mp4")
os.remove(dir_name + f"\\{c}.mp4")
# print(audio_url, type(audio_url))
