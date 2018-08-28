# -*- coding:utf-8 -*-
import os

from scrapy.exporters import CsvItemExporter


PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))


class CsvPipeline(object):
    def open_spider(self, spider):
        # self.file = open("/home/bladestone/enrolldata.csv", "wb")
        self.file = os.path.join(PROJECT_DIR,'media/wealth_csv')
        self.exporter = CsvItemExporter(self.file,
        fields_to_export=[
            'wealth_title',
            'wealth_interest_rate',
            'wealth_sum',
            'wealth_deadline',
            'wealth_starting_amount_or_username',
            'wealth_interest_bearing_method_or_id',
            'wealth_phone_number_or_product_manual',
            'wealth_excepted_return_or_type_of_loan',
            'wealth_redemption_exit_or_use_of_the_loan',
            'wealth_asset_type',
            'wealth_market_value',
            'wealth_payback',
            'wealth_risk_control',
        ])
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
