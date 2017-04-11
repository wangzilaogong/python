# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .sql import Sql
from message.items import MessageItem

class MessagePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,MessageItem):
            href =item['href']
            ret = Sql.select(href)
            if ret[0]==1:
                print('已经存在')
                pass
            else:
                webname=item['webname']
                province=item['province']
                title=item['title']
                href=item['href']
                time = item['time']
                print('开始存储')
        return item
