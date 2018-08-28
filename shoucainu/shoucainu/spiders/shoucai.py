# -*- coding: utf-8 -*-
from scrapy.spider import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

from shoucainu.items import ShoucainuItem


class ShoucaiSpider(CrawlSpider):
    name = 'shoucai'
    start_urls = ['https://www.shoucainu8.com/Invest/llist/status/3']
    rules = (
        Rule(LinkExtractor(allow=(r'https://www.shoucainu8.com/Invest/llist/status/3/p/\d+.html'))),
        Rule(LinkExtractor(allow=(r'https://www.shoucainu8.com/invest/detail/sn/\d+')),
             callback='parse_item')
    )

    def parse_item(self, response):
        sel = Selector(response)
        wealth_title = sel.xpath('//div[@class="invest-title"]/h2/text()')\
            .extract()
        wealth_interest_rate = sel.xpath('//p[@class="rate"]/text()')\
            .extract()
        wealth_sum = sel.xpath('//p[@class="total"]/text()').extract()
        wealth_deadline = sel.xpath('//p[@class="duration"]/text()').extract()
        wealth_starting_amount_or_username = sel\
            .xpath('//table[@class="table-details"]/tr[1]/td/text()').extract()
        wealth_interest_bearing_method_or_id = sel\
            .xpath('//table[@class="table-details"]/tr[2]/td/text()').extract()
        wealth_phone_number_or_product_manual = sel\
            .xpath('//table[@class="table-details"]/tr[3]/td/text()').extract()
        wealth_excepted_return_or_type_of_loan = sel\
            .xpath('//table[@class="table-details"]/tr[4]/td/text()').extract()
        wealth_redemption_exit_or_use_of_the_loan = sel\
            .xpath('//table[@class="table-details"]/tr[5]/td/text()').extract()
        wealth_asset_type = sel\
            .xpath('//table[@class="table-details"]/tr[6]/td/text()').extract()
        wealth_market_value = sel\
            .xpath('//table[@class="table-details"]/tr[7]/td/text()').extract()
        wealth_payback = sel\
            .xpath('//table[@class="table-details"]/tr[8]/td/text()').extract()
        wealth_risk_control = sel\
            .xpath('//table[@class="table-details"]/tr[9]/td/text()').extract()


        item = ShoucainuItem()
        item['wealth_title'] = wealth_title
        item['wealth_interest_rate'] = wealth_interest_rate
        item['wealth_sum'] = wealth_sum
        item['wealth_deadline'] = wealth_deadline
        item['wealth_starting_amount_or_username'] = wealth_starting_amount_or_username
        item['wealth_interest_bearing_method_or_id'] = wealth_interest_bearing_method_or_id
        item['wealth_phone_number_or_product_manual'] = wealth_phone_number_or_product_manual
        item['wealth_excepted_return_or_type_of_loan'] = wealth_excepted_return_or_type_of_loan
        item['wealth_redemption_exit_or_use_of_the_loan'] = wealth_redemption_exit_or_use_of_the_loan
        item['wealth_asset_type'] =  wealth_asset_type
        item['wealth_market_value'] = wealth_market_value
        item['wealth_payback'] = wealth_payback
        item['wealth_risk_control'] = wealth_risk_control
        yield item
