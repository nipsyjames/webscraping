import scrapy

class QuotesSpider(scrapy.spiders.Spider):
     name='quotes'
     start_urls = [
         "http://quotes.toscrape.com/"

     ]
     def parse(self,response):
         title=response.css('title').extract()
         yield {'titletext':title}
