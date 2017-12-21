# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field()
    movie_ename = scrapy.Field()
    movie_type = scrapy.Field()
    movie_publish = scrapy.Field()
    movie_time = scrapy.Field()
    movie_star = scrapy.Field()
    movie_total_price = scrapy.Field()
    pass
