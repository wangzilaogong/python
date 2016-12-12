# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class SecondtryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #字母
    zimu = scrapy.Field()
    #地址
    address = scrapy.Field()


