import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'Quotes'
    start_url = [
        'https://quotes.toscrape.com/'
    ]
    def parse(self,response):
        pass

