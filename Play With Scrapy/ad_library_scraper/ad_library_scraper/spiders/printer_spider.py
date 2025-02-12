import scrapy
import logging
from scrapy_splash import SplashRequest
from ad_library_scraper.items import AdLibraryScraperItem

class PrinterSpider(scrapy.Spider):
    name = "printer_spider"
    start_urls = [
        "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&media_type=video&q=%246%2C400%20subsidy&search_type=keyword_unordered&start_date[min]=2018-05-09&start_date[max]"
    ]

    # script = """
    # function main(splash)
    #     splash:go(splash.args.url)
    #     splash:wait(10)  -- Wait for the dynamic content to load
    #     return {
    #         html = splash:html(),
    #         png = splash:png(),
    #         status = splash.response_status,
    #     }
    # end
    # """

    # def start_requests(self):
    #     for url in self.start_urls:
    #         try:
    #             self.logger.info(f'Sending request to {url}')
    #             yield SplashRequest(url, self.parse, endpoint='execute', args={'lua_source': self.script})
    #         except Exception as e:
    #             self.logger.error(f'Exception in start_requests: {e}')

    # def parse(self, response):
    #     try:
    #         logging.info(f'Received response for {response.url}')
    #         if response.status == 200:
    #             try:
    #                 raw_html = response.text  # This contains the full HTML response
    #                 # Optionally, save the raw HTML to a file for inspection
    #                 with open('raw_response.html', 'w', encoding='utf-8') as f:
    #                     f.write(raw_html)
    #                 item = AdLibraryScraperItem()
    #                 item['library_id'] = response.css('.x67bb7w .x63nzvj.xeuugli::text').get()
    #                 item['started_running_on'] = response.css('.x1crum5w+ div div , .x1e56ztr:nth-child(3) .xeuugli::text').get()
    #                 yield item
    #             except Exception as e:
    #                 logging.error(f'Exception while processing products: {e}')
    #         else:
    #             logging.warning(f'Unexpected status {response.status} for {response.url}')
    #     except Exception as e:
    #         logging.error(f'Exception in parse: {e}')
        
    # def handle_error(self, failure):
    #     logging.error(f'Request failed: {failure}')


    def parse(self, response):
            raw_html = response.text  # This contains the full HTML response
            # Optionally, save the raw HTML to a file for inspection
            with open('raw_response.html', 'w', encoding='utf-8') as f:
                f.write(raw_html)
            item = AdLibraryScraperItem()
            item['library_id'] = response.css('.x67bb7w .x63nzvj.xeuugli::text').get()
            item['started_running_on'] = response.css('.x1crum5w+ div div , .x1e56ztr:nth-child(3) .xeuugli::text').get()
            yield item