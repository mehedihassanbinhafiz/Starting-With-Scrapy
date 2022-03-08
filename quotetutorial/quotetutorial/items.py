# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:  # need to define which item is crawled
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class BinaryQuotes(scrapy.Item):
    quote = scrapy.Field()
    author = scrapy.Field()
