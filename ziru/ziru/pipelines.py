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
            homes = [{
                'ziroom_area': item['ziroom_area'],
                'ziroom_face': item['ziroom_face'],
                'ziroom_floor': item['ziroom_floor'],
                'ziroom_label': item['ziroom_label'],
                # 'ziroom_location': item['ziroom_location'],
                'ziroom_name' :item['ziroom_name'],
                'ziroom_price' : item['ziroom_price'],
                'ziroom_type' : item['ziroom_type'],
                'ziroom_traffic': item['ziroom_traffic'],
                'rounding_info': item['rounding_info'],
                'traffic_info': item['traffic_info'],
                'ziroom_image': item['ziroom_image'],
            }]

            # 插入数据库集合中
            self.collection.insert(homes)
            log.msg('Item wrote to MongoDB database %s/%s' % (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                    level=log.DEBUG, spider=spider)
        return item

