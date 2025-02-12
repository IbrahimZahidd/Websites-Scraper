# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonScraperItem(scrapy.Item):
    title = scrapy.Field()  # Added field for title
    price = scrapy.Field()   # Added field for price
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
