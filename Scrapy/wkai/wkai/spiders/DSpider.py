import scrapy
class DmozSpider(scrapy.Spider):
	"""docstring for DmozSpider"""
	name:"dmoz"
	allow_domains = ["dmoz.org"]
	start_urls =[



	]
	def parse(self,response):
		filename = response.url.split("/")[-2]
		with open(filename,'wb') as f:
			f.write(response.body)
