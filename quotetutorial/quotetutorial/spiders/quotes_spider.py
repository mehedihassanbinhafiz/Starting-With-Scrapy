import scrapy
class QuotesSpider(scrapy.Spider): #scrapy is module Spider is a class
    name = 'Quotes' # the name of the spider
    start_urls = [
        'https://quotes.toscrape.com/'
    ]
    def parse(self,response): # response contains the source code of website
        title = response.css('title::text').extract()
        yield {"titletext ": title} #Generator  # used insted of return



