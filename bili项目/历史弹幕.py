# -*- coding: utf-8 -*-
# @File : 历史弹幕.py
# @Author : 阿波
# @Time : 2023/8/10 14:49
# @Software: PyCharm
import requests

url = 'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=1209265493&date=2023-08-06'
response = requests.get(url)
headers = {
	'Accept': 'application/json, text/plain, */*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
	'Cookie': "buvid3=47CF9962-FBA5-9D9F-9513-437C8F225A6789499infoc; b_nut=1683815889; _uuid=19DC32F7-EC9F-293B-C24B-C9BBD101031E1D90596infoc; buvid4=9A649308-920B-FB2F-7AA6-230794B0E79F94645-023051122-kpAmZQXUvsjZW7nEuBfPBg%3D%3D; i-wanna-go-back=-1; header_theme_version=CLOSE; DedeUserID=88031177; DedeUserID__ckMd5=5a8d915f7318ab03; SESSDATA=0309b2c5%2C1699418555%2Cf8250%2A52; bili_jct=9e943f9b255ca812277e58ed8d8cda9b; rpdid=|(kmJYm|k)k)0J'uY)J)YYlYY; buvid_fp_plain=undefined; b_ut=5; nostalgia_conf=-1; CURRENT_QUALITY=80; CURRENT_PID=b5561d20-fe28-11ed-b76d-b187e758568a; FEED_LIVE_VERSION=V_NO_BANNER_3; CURRENT_FNVAL=4048; sid=69qs8a6r; hit-new-style-dyn=1; hit-dyn-v2=1; LIVE_BUVID=AUTO1516881876003803; bsource=search_bing; bp_article_offset_88031177=815527333630836700; home_feed_column=5; blackside_state=0; CURRENT_BLACKGAP=0; fingerprint=c43e90a6655885155644c5983221544d; buvid_fp=0a9923c6e1eee1d4bd4978b8c9fe2938; b_lsid=55D726E4_189DE08BBF8; browser_resolution=1536-722; PVID=4; bp_video_offset_88031177=828115783979630625",
	'Origin': 'https://www.bilibili.com',
	'Referer': 'https://www.bilibili.com/video/BV1HV411L7Eb/?spm_id_from=333.788&vd_source=bff9605a6957493576220a2ca2264731',
	'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
	'Sec-Ch-Ua-Mobile': '?0',
	'Sec-Ch-Ua-Platform': '"Windows"',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-site',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
}
with open('1.txt', 'w', encoding='utf-8') as f:
	f.write(response.text)
