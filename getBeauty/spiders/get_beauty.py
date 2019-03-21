# -*- coding: utf-8 -*-

import scrapy
import re
from getBeauty.items import GetbeautyItem


class GetBeautySpider(scrapy.Spider):
    name = 'get_beauty'
    start_url = 'http://fun1shot.com/list/1?id=7'
    base_url = 'http://fun1shot.com'

    def start_requests(self):
        yield scrapy.Request(self.start_url, callback=self.parse_urls)

    def parse_urls(self, response):
        # parse article url, and if next page, then parse next page url
        links = response.xpath('//div[@class="row"]/a/@href').extract()
        for link in links:
            url = self.base_url + link
            yield scrapy.Request(url, callback=self.parse_detail)
        re_page = re.search(r'href="(/list/\d+\?id=\d+)">下一頁', response.text, re.S)
        if re_page:
            page_link = re_page.group(1)
            page_url = self.base_url + page_link
            yield scrapy.Request(page_url, callback=self.parse_urls)

    def parse_detail(self, response):
        # parse each url in article
        item = GetbeautyItem()
        img_url_lis = response.xpath('//*[@id="article_content"]/div[2]/img/@src').extract()
        item['img_lis'] = img_url_lis
        yield item
