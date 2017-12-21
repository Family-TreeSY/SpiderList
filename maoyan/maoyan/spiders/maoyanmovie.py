# -*- coding: utf-8 -*-

from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from maoyan.items import MaoyanItem


class MaoyanmovieSpider(CrawlSpider):
    name = 'my'
    # allowed_domains = ['http://maoyan.com/']
    start_urls = ['http://maoyan.com/films']
    rules = (
        Rule(LinkExtractor(allow=(r'http://maoyan.com/films\?offset=\d+'))),
        Rule(LinkExtractor(allow=(r'http://maoyan.com/films/\d+')), callback='parse_item')
    )

    def parse_item(self, response):
        # print(response.body)
        sel = Selector(response)
        movie_name = sel.xpath('/html/body/div[3]/div/div[2]/div[1]/h3/text()').extract()
        movie_ename = sel.xpath('/html/body/div[3]/div/div[2]/div[1]/div/text()').extract()
        movie_type = sel.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/text()').extract()
        movie_publish = sel.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[2]/text()').extract()
        movie_time = sel.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()').extract()
        movie_star = sel.xpath('/html/body/div[3]/div/div[2]/div[3]/div[1]/div/span/span/text()').extract()
        # movie_total_price = sel.xpath('/html/body/div[3]/div/div[2]/div[3]/div[2]/div/span[1]/text()').extract()
        # movie_introd = sel.xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/span/text()').extract()
        # print(movie_name)
        # print(movie_ename)
        # print(movie_type)
        # print(movie_publish)
        # print(movie_time)
        # print(movie_star)
        # print(movie_total_price)

        item = MaoyanItem()
        item['movie_name'] = movie_name
        item['movie_ename'] = movie_ename
        item['movie_type'] = movie_type
        item['movie_publish'] = movie_publish
        item['movie_time'] = movie_time
        item['movie_star'] = movie_star
        # item['movie_total_price'] = movie_total_price
        # item['movie_introd'] = movie_introd

        yield item
