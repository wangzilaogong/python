# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MessageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()#网站名

    url = scrapy.Field()#超链接

    title =scrapy.Field()#标题

    href = scrapy.Field()#标题超链接

    time = scrapy.Field()#发布时间


