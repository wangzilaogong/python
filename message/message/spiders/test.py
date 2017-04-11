import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from message.items import MessageItem
import lxml

#myspider
class Myspider(scrapy.Spider):

    name = 'message'
    start_urls={
      "http://www.tjconstruct.cn/zbxx.aspx?type=sjzb"
    }
    def parse(self, response):

       time = response.xpath('//div[@class="a09" and @align="right"]/text()').extract()

       print(time)