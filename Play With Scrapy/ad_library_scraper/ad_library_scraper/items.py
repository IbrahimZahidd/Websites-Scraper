# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AdLibraryScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    library_id = scrapy.Field()  # Field for Library ID
    started_running_on = scrapy.Field()  # Field for Started Running Date
