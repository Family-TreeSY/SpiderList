# -*- coding: utf-8 -*-

from scrapy.spiders import Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from ziru.items import ZiruItem
from scrapy_redis.spiders import RedisCrawlSpider


class ZiroomSpider(RedisCrawlSpider):
    name = 'ziroom'
    # allowed_domains = ['http://sh.ziroom.com/z/nl/z2.html?qwd=']
    # start_urls = ['http://sh.ziroom.com/z/nl/z2.html?qwd=']
    redis_key = 'ziroomspider:start_urls'
    rules = (
        Rule(LinkExtractor(allow=(r'http://sh.ziroom.com/z/nl/z2.html\?qwd=\&p=\d+'))),
        Rule(LinkExtractor(allow=(r'http:\//sh\.ziroom\.com\/z\/vr\/\d+\.html')), callback='parse_item')
    )

    def parse_item(self, response):
        # print(response.body)
        sel = Selector(response)
        ziroom_name = sel.xpath('//div[@class="room_name"]/h2/text()').extract()
        # ziroom_location = sel.xpath('//span[@class="ellipsis"]/text()').extract()
        ziroom_price = sel.xpath('//*[@id="room_price"]/text()').extract()
        ziroom_label1 = sel.xpath('//p[@class="room_tags clearfix"]/span[@class="balcony"]/text()').extract()
        ziroom_label2 = sel.xpath('//p[@class="room_tags clearfix"]/a/span[@class="style"]/text()').extract()
        ziroom_area = sel.xpath('//ul[@class="detail_room"]/li[1]/text()').extract()
        ziroom_face = sel.xpath('//ul[@class="detail_room"]/li[2]/text()').extract()
        ziroom_type = sel.xpath('//ul[@class="detail_room"]/li[3]/text()').extract()
        ziroom_floor = sel.xpath('//ul[@class="detail_room"]/li[4]/text()').extract()
        ziroom_traffic = sel.xpath('//ul[@class="detail_room"]/li[@class="last"]/span/text()').extract()
        rounding_info = sel.xpath('//div[@class="aboutRoom gray-6"]/p[1]/text()').extract()
        traffic_info = sel.xpath('//div[@class="aboutRoom gray-6"]/p[2]/text()').extract()
        ziroom_image = sel.xpath('//*[@id="cao"]/ul/li[10]/a/@href').extract()


        # print(ziroom_area)
        # print(ziroom_face)
        # print(ziroom_floor)
        # print(ziroom_label1)
        # print(ziroom_label2)
        # # print(ziroom_location)
        # print(ziroom_name)
        # print(ziroom_price)
        # print(ziroom_type)
        # print(ziroom_traffic)
        # print(rounding_info)
        # print(traffic_info)
        # print(ziroom_image)

        item = ZiruItem()

        item['ziroom_name'] = ziroom_name
        item['ziroom_price'] = ziroom_price
        item['ziroom_label'] = ziroom_label1 + ziroom_label2
        item['ziroom_area'] = ziroom_area
        item['ziroom_face'] = ziroom_face
        item['ziroom_type'] = ziroom_type
        item['ziroom_floor'] = ziroom_floor
        item['ziroom_traffic'] = ziroom_traffic
        item['rounding_info'] = rounding_info
        item['traffic_info'] = traffic_info
        item['ziroom_image'] = ziroom_image

        yield item

