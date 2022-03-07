
import scrapy
from ..items import QuotetutorialItem
from scrapy.http import FormRequest

class QuotesSpider(scrapy.Spider): #scrapy is module Spider is a class
    name = 'quotes_login' # the name of the spider
    page_number = 0
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]
    def parse(self,response): # response contains the source code of website
        token = response.css('form input::attr(value)').extract_first()

        return FormRequest.from_response(response, formdata={
            'csrf_token':token,
            'username':'haha',
            'password':'haha',
        }, callback = self.start_scraping)

    def start_scraping(self, response):
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
        if QuotesSpider.page_number == 0:
            next_page = 'https://quotes.toscrape.com'
        else:
            next_page = 'https://quotes.toscrape.com/page/{}/'.format(QuotesSpider.page_number)
            print(next_page)
        if QuotesSpider.page_number < 10: #response.follow() # scrapy used it for next page
            QuotesSpider.page_number += 1
            yield response.follow(next_page, callback = self.start_scraping)







