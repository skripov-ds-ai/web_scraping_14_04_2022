# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import json

import scrapy
from scrapy.loader.processors import Compose, Join, MapCompose, TakeFirst


def create_img_urls_array(info_strings):
    infos = json.loads(info_strings[0])
    print()
    return [info["full"] for info in infos]


def clear_string(s):
    return s.strip()


class LabirintItem(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(
        input_processor=MapCompose(clear_string),
        output_processor=Join(separator=" ")
    )
    prices = scrapy.Field(input_processor=MapCompose(clear_string))
    main_img_url = scrapy.Field(output_processor=TakeFirst())
    img_urls = scrapy.Field(input_processor=Compose(create_img_urls_array))
    img_info = scrapy.Field()
