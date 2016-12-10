import  re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request ##一个单独的request模块，需要跟进的时候需要它
from secondtry.items import SecondtryItem##自定义保存的字段

#Spider
class Myspider(scrapy.Spider):
    name = 'secondtry'
    allowed_domains=['shuifeng.net']
    bash_url ='http://www.shuifeng.net/Dic/Html/'
    bashurl='.htm'


    def start_requests(self):
        for i in range(1,2501):
            url = self.bash_url +'P'+ str(i) + self.bashurl
            print(url)
            yield Request(url,self.parse)
        yield Request('http://www.shuifeng.net/Dic/Html/Index.htm',self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        print (soup.title)


