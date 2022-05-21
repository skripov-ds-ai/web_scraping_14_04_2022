import scrapy
from scrapy.http import TextResponse
from scrapy.loader import ItemLoader

from labirint.items import LabirintItem


class LabirintruSpider(scrapy.Spider):
    name = 'labirintru'
    allowed_domains = ['labirint.ru']

    def __init__(self, search):
        super().__init__()
        self.start_urls = [
            f"https://www.labirint.ru/search/{search}/?stype=0"
        ]

    def parse(self, response: TextResponse, **kwargs):
        print()
        item_urls = response.xpath(
            '//div[contains(@class, "need-watch")]'
            '//a[contains(@class, "product-title-link")]/@href'
        ).getall()
        for item_url in item_urls:
            yield response.follow(item_url, callback=self.parse_item)

    def parse_item(self, response: TextResponse):
        product_xpath = '//div[@id="product"]'
        prices_xpath = f'{product_xpath}' \
                       f'//div[contains(@class, "buying-price") and ' \
                       f'contains(@class, "-val")]//text()'
        title_xpath = f'{product_xpath}//div[@id="product-title"]/h1//text()'
        # main_img_url_xpath = f'{product_xpath}' \
        #                      f'//div[@id="product-image"]' \
        #                      f'/img/@src'
        main_img_url_xpath = f'{product_xpath}' \
                             f'//div[@id="product-image"]' \
                             f'/img/@data-src'
        screenshot_info_xpath = '//div[@id="product-screenshot"]/@data-source'

        loader = ItemLoader(item=LabirintItem(), response=response)
        loader.add_value("url", response.url)
        loader.add_xpath("title", title_xpath)
        loader.add_xpath("prices", prices_xpath)
        loader.add_xpath("main_img_url", main_img_url_xpath)
        loader.add_xpath("img_urls", screenshot_info_xpath)

        yield loader.load_item()
