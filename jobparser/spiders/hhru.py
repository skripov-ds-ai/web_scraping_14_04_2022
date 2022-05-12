import scrapy
from scrapy.http import TextResponse

from jobparser.items import JobparserItem

TEMPLATE_URL = "https://omsk.hh.ru/search/vacancy?text="


class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    max_page_number = 2
    # start_urls = [
    #     'https://omsk.hh.ru/search/vacancy'
    #     '?text=python&from=suggest_post&fromSearchLine=true&area=160'
    # ]

    def __init__(self, query, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [TEMPLATE_URL + query]

    def parse_item(self, response: TextResponse):
        # print("PARSE_ITEM")
        # print()
        title_xpath = '//h1[@data-qa="vacancy-title"]//text()'
        salary_xpath = '//span[contains(@data-qa, "salary")]//text()'
        title = response.xpath(title_xpath).getall()
        salary = response.xpath(salary_xpath).getall()
        item = JobparserItem()
        item["title"] = title
        item["salary"] = salary
        item["url"] = response.url
        # item['abc'] = 42
        # print()
        yield item

    def parse(self, response: TextResponse, page_number: int = 1, **kwargs):
        # print(f"PAGE_NUMBER = {page_number}")
        items = response.xpath('//a[contains(@data-qa, "__vacancy-title")]')
        # первые 2 вакансии для примера
        for item in items[:2]:
            url = item.xpath("./@href").get()
            yield response.follow(url, callback=self.parse_item)
        #     print()
        # print("---")
        # print()
        next_url_xpath = '//a[contains(@data-qa, "pager-next")]/@href'
        next_url = response.xpath(next_url_xpath).get()
        # if next_url:
        if next_url and page_number < self.max_page_number:
            new_kwargs = {
                "page_number": page_number + 1,
            }
            yield response.follow(
                next_url,
                callback=self.parse,
                cb_kwargs=new_kwargs
            )
