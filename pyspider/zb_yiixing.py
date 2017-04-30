#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-04-25 11:31:29
# Project: zb_yixing

from pyspider.libs.base_handler import *
from pyspider.database.mysql.mysqldb import SQL

class Handler(BaseHandler):
    crawl_config = {
    }
       
    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.yxztb.net/yxweb/zypd/012001/012001001/', callback=self.index_page)

    @config(age=60 * 60)
    def index_page(self, response):
        for each in response.doc('.tdmoreinfosub a').items():
            self.crawl(each.attr.href, callback=self.detail_page)
            
    @config(priority=2)
    def detail_page(self, response):
        
        return {
                "address":"宜兴市",
                "url":response.url,
                "title":response.doc('font  span').text(),
                "date" :response.doc('#tdTitle > .webfont').text()[8:17],
            }
    
    def on_result(self, result):
        print result
        if not result or not result['title']:
            return
        sql = SQL()
        sql.replace('zhaobiao',**result)
 

    