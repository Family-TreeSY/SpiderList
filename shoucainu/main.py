# -*- coding:utf-8 -*-
from scrapy import cmdline

cmdline.execute("scrapy crawl shoucai -o wealth.csv -t csv".split())
