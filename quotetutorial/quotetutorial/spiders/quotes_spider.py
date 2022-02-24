import scrapy
from ..items import QuotetutorialItem
class QuotesSpider(scrapy.Spider): #scrapy is module Spider is a class
    name = 'quotes' # the name of the spider
    start_urls = [
        'https://quotes.toscrape.com/'
    ]
    def parse(self,response): # response contains the source code of website

        quote_item = QuotetutorialItem()

        all_quotes = response.css("div.quote")
        for c_quote in all_quotes:
            quote = c_quote.css("span.text::text").extract()
            author = c_quote.css("small.author::text").extract()
            tag = c_quote.css("a.tag::text").extract()
            quote_item['title'] = quote
            quote_item['author'] = author
            quote_item['tags'] = tag
            yield quote_item#Generator  # used insted of return



