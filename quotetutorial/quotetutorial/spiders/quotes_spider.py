import scrapy
from ..items import QuotetutorialItem
class QuotesSpider(scrapy.Spider): #scrapy is module Spider is a class
    name = 'quotes' # the name of the spider
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
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
            yield quote_item#Generator  # used insted of return. it returns value one by one

        next_page = 'https://quotes.toscrape.com/page/{}/'.format(QuotesSpider.page_number)
        if QuotesSpider.page_number < 5: #response.follow() # scrapy used it for next page
            QuotesSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)






