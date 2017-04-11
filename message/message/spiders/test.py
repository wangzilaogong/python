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
    baseurl ='http://www.tjconstruct.cn/'
    start_urls={
      "http://www.tjconstruct.cn/zbxx.aspx?type=sjzb"
    }
    def parse(self, response):
        times = response.xpath('//div[@class="a09" and @align="right"]/text()').extract()
        titles = response.xpath('//a[@class="a09" and @target="_blank"]/text()').extract()
        hrefs =response.xpath('//a[@class="a09" and @target="_blank"]/@href').extract()
        for href in hrefs:
            print(self.baseurl+href)
        for title in titles:
            print(title)
        for time in times:
            print(time)