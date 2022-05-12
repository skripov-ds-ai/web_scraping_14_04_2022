from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

# from jobparser.spiders.sjru import SuperJobSpider
from jobparser import settings
from jobparser.spiders.hhru import HhruSpider

if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)

    hhru_kwargs = {"query": "python"}
    process.crawl(HhruSpider, **hhru_kwargs)
    # process.crawl(SuperJobSpider)

    process.start()
