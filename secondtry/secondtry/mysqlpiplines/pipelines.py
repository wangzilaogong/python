# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .sql import Sql
from secondtry.items import SecondtryItem

class SecondtryPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,SecondtryItem):
            title = item['zimu']
            address = item['address']
            Sql.insert_dd_name(title,address)
            print('ok')
