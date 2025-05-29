# -*- coding: utf-8 -*-
"""
Created on 2025-05-21 22:08:50
---------
@summary:
---------
@author: lan
"""

import feapder
from feapder.utils.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Baidu(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://www.baidu.com",render=True)

    def parse(self, request, response):
        browser: WebDriver = response.browser
        browser.find_element(By.ID, 'kw').send_keys('feapder')
        browser.find_element(By.ID, 'su').click()


if __name__ == "__main__":
    Baidu().start()