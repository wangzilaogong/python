import scrapy
import  re
from bs4 import BeautifulSoup
from middle.items import MiddleItem


class MiddleSpifer(scrapy.Spider):
    name = 'middle'
    start_urls={
        "http://www.tjztb.gov.cn/zbgg/gczb/"



    }

    def parse(self, response):
        date=  re.findall('<span>(.*?)</span>',response.text)
        hrefall = re.findall('<li>(.*?)</li>',response.text)

        for i in range(1,10):
            print(date[i])
            print(hrefall[i+6])







