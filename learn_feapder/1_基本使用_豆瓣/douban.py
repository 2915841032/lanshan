# -*- coding: utf-8 -*-

import feapder
from douban_item import DoubanItem



class Douban(feapder.AirSpider):
    def start_requests(self):
        for page in range(10):
            yield feapder.Request(f'https://movie.douban.com/top250?start={page * 25}&filter=')

    def parse(self, request, response):
        li_list = response.xpath('//ol/li/div[@class="item"]')
        for li in li_list:
            item = DoubanItem()
            item['title'] = li.xpath('./div[@class="info"]/div/a/span[1]/text()').extract_first()
            item['detail_url'] = li.xpath('./div[@class="info"]/div/a/@href').extract_first()
            item['score'] = li.xpath('.//div[@class="star"]/span[2]/text()').extract_first()
            yield feapder.Request(item['detail_url'], callback=self.detail_parse, item=item)

    def detail_parse(self, request, response):
        if response.xpath('//div[@class="indent"]/span[@class="all hidden"]//text()'):
            request.item['detail_text'] = response.xpath(
                '//div[@class="indent"]/span[@class="all hidden"]//text()').extract_first().strip()
        else:
            request.item['detail_text'] = response.xpath(
                '//div[@class="indent"]/span[1]//text()').extract_first().strip()

        # 进行数据入库
        yield request.item
        





if __name__ == "__main__":
    Douban().start()