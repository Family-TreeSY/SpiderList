# _*_ coding=utf-8 _*_

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from douban.items import DoubanItem
from scrapy.http import Request


class DouBanSpider(CrawlSpider):
    name = 'db'
    start_urls = ['https://movie.douban.com/top250']

    url = 'http://movie.douban.com/top250'

    def parse(self, response):
        # print(response.body)
        item = DoubanItem()
        selector = Selector(response)

        # print(selector)
        movies = selector.xpath('//div[@class="info"]')
        for movie in movies:
            movie_name = movie.xpath('div[@class="hd"]/a/span/text()').extract()
            movie_star = movie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            movie_quote = movie.xpath('div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract()

            #print(movie_name)
            #print(movie_star)
            #print(movie_quote)


            item['movie_name'] = movie_name
            item['movie_star'] = movie_star
            item['movie_quote'] = movie_quote
            yield item
            #print(movie_name)
            #print(movie_star)
            #print(movie_quote)

            next_page = selector.xpath('//span[@class="next"]/link/@href').extract()
            if next_page:
                next_page = next_page[0]
                print(next_page)
                yield Request(self.url + next_page, callback=self.parse)




