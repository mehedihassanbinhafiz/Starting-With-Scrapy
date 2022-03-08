
import scrapy

class BinarySpider(scrapy.Spider):
    name = 'binary'
    start_urls = [
        'https://www.brainyquote.com/topics/binary-quotes'
    ]
    def parse(self, response):
        all_quotes = response.css("div.grid-item.qb.clearfix.bqQt")
        print(len(all_quotes))
        for quotes_element in all_quotes:
            quote = quotes_element.css("div::text").extract()
            quote = ''.join([x.strip() for x in quote])
            author = quotes_element.css("a::text").extract()
            author = ''.join(x.strip() for x in author)
            print('quotes: ',quote, 'author: ',author)
