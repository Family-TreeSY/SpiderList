# -*- coding:utf-8 -*-

from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from douban_movie.items import DoubanMovieItem


class Douban(CrawlSpider):
    name = 'db'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']
    rules = (
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/top250\?start=\d+&filter='))),
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/subject/\d+')), callback='parse_item')

    )

    def parse_item(self, response):
        sel = Selector(response)
        item = DoubanMovieItem()
        title = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        director = sel.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        actor = sel.xpath('//*[@id="info"]/span[3]/span[2]/a/text()').extract()
        #release_time = sel.xpath('//*[@id="info"]/span[11]/text()').extract()
        #time = sel.xpath('//*[@id="info"]/span[13]/text()').extract()
        star = sel.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()


        item['title'] = title
        item['director'] = director
        item['actor'] = actor
        #item['release_time'] = release_time
        #item['time'] = time
        item['star'] = star

        yield item

        #print(title)
        #print(director)
        #print(actor)
        #print(release_time)
        #print(time)
        #print(star)
#
