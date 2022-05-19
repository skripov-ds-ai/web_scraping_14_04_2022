import os

from dotenv import load_dotenv
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from vc import settings
from vc.spiders.vcru import VcruSpider

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


if __name__ == "__main__":
    custom_settings = Settings()
    custom_settings.setmodule(settings)

    process = CrawlerProcess(settings=custom_settings)
    process.crawl(VcruSpider, login=EMAIL, password=PASSWORD)

    process.start()
