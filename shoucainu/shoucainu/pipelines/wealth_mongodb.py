# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
import datetime


class   MongoDBPipeline(object):
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
            wealth = [{
                'wealth_title': item['wealth_title'],
                'wealth_interest_rate': item['wealth_interest_rate'],
                'wealth_sum': item['wealth_sum'],
                'wealth_deadline': item['wealth_deadline'],
                'wealth_starting_amount_or_username': item['wealth_starting_amount_or_username'],
                'wealth_interest_bearing_method_or_id': item['wealth_interest_bearing_method_or_id'],
                'wealth_phone_number_or_product_manual': item['wealth_phone_number_or_product_manual'],
                'wealth_excepted_return_or_type_of_loan': item['wealth_excepted_return_or_type_of_loan'],
                'wealth_redemption_exit_or_use_of_the_loan': item['wealth_redemption_exit_or_use_of_the_loan'],
                'wealth_asset_type': item['wealth_asset_type'],
                'wealth_market_value': item['wealth_market_value'],
                'wealth_payback': item['wealth_payback'],
                'wealth_risk_control': item['wealth_risk_control'],
            }]

            # 插入数据库集合中
            self.collection.insert(wealth)
            log.msg('Item wrote to MongoDB database %s/%s' % (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                    level=log.DEBUG, spider=spider)
        return item