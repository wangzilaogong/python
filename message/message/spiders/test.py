import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from message.items import MessageItem
import lxml


#myspider
class Myspider(scrapy.Spider):
    name = 'message'
    webname ='天津建设工程信息网'
    province ='天津市'
    baseurl ='http://www.tjconstruct.cn/'
    start_urls={
      "http://www.tjconstruct.cn/zbxx.aspx"
    }
    def parse(self, response):
        times = response.xpath('//div[@class="a09" and @align="right"]/text()').extract()
        titles = response.xpath('//a[@class="a09" and @target="_blank"]/text()').extract()
        hrefs =response.xpath('//a[@class="a09" and @target="_blank"]/@href').extract()

    def get(self,response):
        item = MessageItem()
        item['webname']=self.webname
        item['province']=self.province

        return item
