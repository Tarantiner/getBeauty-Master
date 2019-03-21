# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import pymongo
import requests
from concurrent.futures import ThreadPoolExecutor


class SaveUrlpipeline(object):
    client = None
    db = None
    collection_name = 'rihan'

    def __init__(self, mongo_uri, mongo_database):
        self.mongo_uri = mongo_uri
        self.mongo_database = mongo_database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings.get('MONGO_URI'),
            crawler.settings.get('MONGO_DATABASE'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_database]

    def process_item(self, item, spider):
        for url in item['img_lis']:
            self.db[self.collection_name].insert({'img_url': url})
        return item

    def close_spider(self, spider):
        self.client.close()


class SaveImgpipeline(object):

    def open_spider(self, spider):
        if not os.path.exists('imgs/rihan'):
            os.makedirs('imgs/rihan')

    def dlimg(self, url):
        img_name = url.split('/')[-1]
        content = requests.get(url=url).content
        with open(f'imgs/rihan/{img_name}', 'wb') as fp:
            fp.write(content)

    def process_item(self, item, spider):
        pool = ThreadPoolExecutor(10)
        for url in item['img_lis']:
            pool.submit(self.dlimg, url)
        return item


