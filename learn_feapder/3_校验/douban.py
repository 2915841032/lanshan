# -*- coding: utf-8 -*-
"""
Created on 2025-05-21 21:58:58
---------
@summary:
---------
@author: lan
"""

import feapder


class Douban(feapder.AirSpider):
    def download_midware(self, request):
        request.proxies = {
            'http': 'http://127.0.0.1:7980'
        }
        return request

    def start_requests(self):
        yield feapder.Request("https://movie.douban.com/top250?start=0&filter=",verify=False)

    def validate(self, request, response):
        # print('响应状态码:', response.status_code)
        if response.status_code != 200:
            print('响应状态码异常:', response.status_code)
            return False  # 抛弃当前请求
            # raise Exception('请求重试')

    def parse(self, request, response):
        pass


if __name__ == "__main__":
    Douban().start()