# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShoucainuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    wealth_title = scrapy.Field()
    wealth_interest_rate = scrapy.Field()
    wealth_sum = scrapy.Field()
    wealth_deadline = scrapy.Field()
    # 起头金额或用户名字
    wealth_starting_amount_or_username = scrapy.Field()
    # 计息方式或身份证
    wealth_interest_bearing_method_or_id = scrapy.Field()
    # 产品说明或者手机号码
    wealth_phone_number_or_product_manual = scrapy.Field()
    # 预期收益或借款金额
    wealth_excepted_return_or_type_of_loan = scrapy.Field()
    # 赎回退出或者借款用途
    wealth_redemption_exit_or_use_of_the_loan = scrapy.Field()
    #资产种类
    wealth_asset_type = scrapy.Field()
    #市场价值
    wealth_market_value = scrapy.Field()
    # 还款能力
    wealth_payback = scrapy.Field()
    # 风险控制
    wealth_risk_control = scrapy.Field()
    pass
