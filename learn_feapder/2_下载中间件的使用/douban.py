# -*- coding: utf-8 -*-
"""
Created on 2025-05-21 21:46:55
---------
@summary:
---------
@author: lan
"""

import feapder


class Douban(feapder.AirSpider):
    def custom_download_midware(self, request):
        print("下载中间件")
        request.headers= {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            'a':'b'
        }
        request.proxies = {
                'http': 'http://127.0.0.1:7980'
            }


        return request


    def start_requests(self):
        yield feapder.Request("https://www.google.com/?hl=zh_CN",download_midware=self.custom_download_midware)


    def parse(self, request, response):
        print(response.text)







if __name__ == "__main__":
    Douban().start()