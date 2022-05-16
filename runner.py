from urllib import parse

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from otparser import settings
from otparser.spiders.online_trade import OnlineTradeSpider

# from jobparser.spiders.sj import SuperJobSpider

# https://www.onlinetrade.ru/sitesearch.html?query=
# %EC%E0%F2%E5%F0%E8%ED%F1%EA%E0%FF+%EF%EB%E0%F2%E0+asus

if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    # TODO: customize it
    search = "материнская плата asus"
    search = parse.quote_plus(search.encode("cp1251"))

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(OnlineTradeSpider, query=search)
    process.start()
