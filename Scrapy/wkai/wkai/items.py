# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WkaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    #标题链接
    address = scrapy.Field()
    #时间
    date = scrapy.Field()
    #状态
    serialstatus = scrapy.Field()

