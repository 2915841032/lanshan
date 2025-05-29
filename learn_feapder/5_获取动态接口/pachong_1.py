# -*- coding: utf-8 -*-
"""
Created on 2025-05-21 22:15:09
---------
@summary:
---------
@author: lan
"""

import feapder
from feapder.utils.webdriver import WebDriver


class Pachong1(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://spidertools.cn", render=True)

    def parse(self, request, response):
        browser: WebDriver = response.browser
        # ad = browser.xhr_text('/ad')
        # print(ad)

        xhr_response = browser.xhr_response("/ad")
        print("请求接口", xhr_response.request.url)
        # 请求头目前获取的不完整
        print("请求头", xhr_response.request.headers)
        print("请求体", xhr_response.request.data)
        print("返回头", xhr_response.headers)
        print("返回地址", xhr_response.url)
        print("返回内容", xhr_response.content)


if __name__ == "__main__":
    Pachong1().start()