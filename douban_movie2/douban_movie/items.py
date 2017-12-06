# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    release_time = scrapy.Field()
    time = scrapy.Field()
    star = scrapy.Field()
