# -*- coding: utf-8 -*-
"""
Created on 2025-05-21 22:37:37
---------
@summary:
---------
@author: lan
"""

import time
import feapder
from random import randint
from items.wp_shop_info_item import WpShopInfoItem
from selenium.webdriver.common.by import By
from feapder.utils.webdriver import WebDriver

from feapder import setting


class WpShop(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://category.vip.com/suggest.php?keyword=%E7%94%B5%E8%84%91&ff=235|12|1|1",
                              render=True)

    def parse(self, request, response):
        browser: WebDriver = response.browser
        time.sleep(2)

        # 页面动态下滑以加载数据
        self.drop_down(browser)

        # 获取页面中所有的商品div
        div_list = browser.find_elements(By.XPATH,
                                         '//section[@id="J_searchCatList"]/div[@class="c-goods-item  J-goods-item c-goods-item--auto-width"]')
        # print(div_list)

        # 对返回的div_list进行迭代并获取每个商品的信息
        for div in div_list:
            item = WpShopInfoItem()
            title = div.find_element(By.XPATH, './/div[2]/div[2]').text
            price = div.find_element(By.XPATH,
                                     './/div[@class="c-goods-item__sale-price J-goods-item__sale-price"]').text
            item['title'] = title
            item['price'] = price

            # MySQL数据库自动入库
            yield item

        # 翻页
        self.next_page(browser)
        next_url = browser.current_url  # 获取翻页后的网页地址
        yield feapder.Request(next_url, render=True, callback=self.parse)

    def drop_down(self, browser):
        for i in range(1, 12):
            js_code = f'document.documentElement.scrollTop = {i * 1000}'
            browser.execute_script(js_code)
            time.sleep(randint(1, 2))

    def next_page(self, browser):
        try:
            next_button = browser.find_element(By.XPATH, '//*[@id="J_nextPage_link"]')
            if next_button:
                next_button.click()
            else:
                browser.close()
        except Exception as e:
            print('最后一页: ', e)
            browser.quit()


if __name__ == "__main__":
    WpShop().start()