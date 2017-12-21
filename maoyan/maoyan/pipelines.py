# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log



class MongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = client[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]


    def process_item(self, item, spider):
        # item:  (Item 对象) – 被爬取的item
        # (Spider 对象) – 爬取该item的spider
        # 去重，删除重复的数据
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('Missing %s of blogpost from %s' % (data, item['url']))
        if valid:
            movies = [{
                'movie_name': item['movie_name'],
                'movie_ename': item['movie_ename'],
                'movie_type': item['movie_type'],
                'movie_publish': item['movie_publish'],
                'movie_time': item['movie_time'],
                'movie_star': item['movie_star']
            }]
            # 插入数据库集合中
            self.collection.insert(movies)
            log.msg('Item wrote to MongoDB database %s/%s' % (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                    level=log.DEBUG, spider=spider)
        return item
