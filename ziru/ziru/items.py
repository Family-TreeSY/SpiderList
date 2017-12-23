# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZiruItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ziroom_area = scrapy.Field()
    ziroom_face = scrapy.Field()
    ziroom_floor = scrapy.Field()
    ziroom_label = scrapy.Field()
    # ziroom_location = scrapy.Field()
    ziroom_name = scrapy.Field()
    ziroom_price = scrapy.Field()
    ziroom_type = scrapy.Field()
    ziroom_traffic = scrapy.Field()
    rounding_info = scrapy.Field()
    traffic_info = scrapy.Field()
    ziroom_image = scrapy.Field()
    pass
