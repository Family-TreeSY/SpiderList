# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from scrapy import log
from scrapy.conf import settings


class MongoDBPipeline(object):
    # 连接到MongoDB数据库
    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        # 删除错误数据
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('Missing %s of blogpost from %s' % (data, item['url']))
        if valid:
            movies = [{
                'title': item['title'],
                'director': item['director'],
                'actor': item['actor'],
                'star': item['star']
            }]
            self.collection.insert(movies)
            log.msg("Item wrote to MongoDB database %s/%s" %
            (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
            level=log.DEBUG, spider=spider)

        return item
