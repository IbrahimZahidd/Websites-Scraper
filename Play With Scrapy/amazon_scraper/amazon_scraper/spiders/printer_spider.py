import scrapy
from amazon_scraper.items import AmazonScraperItem

class PrinterSpider(scrapy.Spider):
    name = "printer_spider"
    start_urls = [
        "https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172635&ref=nav_em__nav_desktop_sa_intl_printers_0_2_6_11"
    ]

    def parse(self, response):
        for product in response.css('.s-main-slot .s-result-item'):
            item = AmazonScraperItem()
            item['title'] = product.css('.a-color-base.a-text-normal::text').get()
            item['price'] = product.css('.a-price-fraction, .a-price-whole::text').get()  # Updated price selector
            yield item