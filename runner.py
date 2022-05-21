from urllib.parse import quote

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from labirint import settings
from labirint.spiders.labirintru import LabirintruSpider


if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    search = "смарт-контракты"
    search = quote(search)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LabirintruSpider, search=search)

    process.start()
