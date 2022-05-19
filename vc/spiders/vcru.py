import json
from pprint import pprint

import scrapy
from scrapy import Selector
from scrapy.http import FormRequest, TextResponse

from vc.items import VcItem


# scrapy-rotating-proxy и scrapy-rotated-proxy
class VcruSpider(scrapy.Spider):
    name = "vcru"
    allowed_domains = ["vc.ru"]
    start_urls = ["https://vc.ru/"]
    login_url = "https://vc.ru/auth/simple/login"
    interesting_url = "https://vc.ru/marketing"
    max_posts_page_number = 5
    template_url = (
        "https://vc.ru/marketing/more?"
        "last_id=%s&last_sorting_value=%s"
        "&page=%s&exclude_ids=[]&mode=raw"
    )

    def __init__(self, login, password):
        super().__init__()
        self.login = login
        self.password = password

    def parse(self, response: TextResponse, **kwargs):
        print("PARSE")
        print()
        print(response.url)
        version = response.xpath(
            "//link[@rel='stylesheet'" " and contains(@href, 'vc-')]/@href"
        ).get()
        version = version.split("/")[-1].split(".")[1]
        print()
        yield FormRequest(
            self.login_url,
            formdata={
                "values[login]": self.login,
                "values[password]": self.password,
                "mode": "raw",
            },
            headers={
                "origin": response.url,
                "referer": response.url,
                "x-js-version": version,
                "x-this-is-csrf": "THIS IS SPARTA!",
            },
            callback=self.parse_login,
            method="POST",
        )

    def parse_login(self, response: TextResponse):
        print("PARSE_LOGIN")
        print()
        data = response.json()
        if data["rc"] != 200:
            raise ValueError(f"Something went wrong with login: {data['rm']}")
        yield response.follow(self.interesting_url, callback=self.parse_posts)

    def parse_posts(self, response: TextResponse):
        print("POSTS")
        posts = response.xpath("//div[@data-location='my-feed']")
        for post in posts:
            # "//a[@class='content-link']/@href"
            item = VcItem()
            item["url"] = post.xpath(".//a[@class='content-link']/@href").get()
            item["title"] = post.xpath(
                './/div[contains(@class, "content-title")]//text()'
            ).getall()
            yield item

        print()

        last_id_xpath = "//div[@class='feed']/@data-feed-last-id"
        last_id = response.xpath(last_id_xpath).get()
        # data-feed-last-sorting-value
        last_sorting_value = response.xpath(
            "//div[@class='feed']/@data-feed-last-sorting-value"
        ).get()
        next_page_number = 2
        new_url = self.template_url % (
            last_id,
            last_sorting_value,
            str(next_page_number),
        )
        yield response.follow(
            new_url,
            callback=self.parse_ajax_posts,
            method="GET",
            headers={
                "referer": "https://vc.ru/marketing",
            },
            cb_kwargs={
                "page_number": next_page_number,
            },
        )

    def parse_ajax_posts(self, response: TextResponse, page_number: int):
        print("AJAX")
        print(f"Page number = {page_number}")
        data = {}
        try:
            data = response.json()
        except json.JSONDecodeError as e:
            print(e)
            print(f"Page number = {page_number} was the last.")
            return

        if (
            "rc" not in data
            or data["rc"] != 200
            or "data" not in data
            or not data["data"]
            or "items_html" not in data["data"]
        ):
            print("DATA:")
            pprint(data)
            print(f"Page number = {page_number} was the last.")
            return

        html_data = data["data"]["items_html"]
        sel = Selector(text=html_data)
        posts = sel.xpath("//div[@data-location='my-feed']")
        print()
        for post in posts:
            # "//a[@class='content-link']/@href"
            item = VcItem()
            item["url"] = post.xpath(".//a[@class='content-link']/@href").get()
            item["title"] = post.xpath(
                './/div[contains(@class, "content-title")]//text()'
            ).getall()
            yield item

        print()
        last_id = data["data"]["last_id"]
        last_sorting_value = data["data"]["last_sorting_value"]
        next_page_number = page_number + 1
        if next_page_number < self.max_posts_page_number:
            print(f"Moving to page with number = {next_page_number}...")
            new_url = self.template_url % (
                last_id,
                last_sorting_value,
                str(next_page_number),
            )
            yield response.follow(
                new_url,
                callback=self.parse_ajax_posts,
                method="GET",
                headers={
                    "referer": "https://vc.ru/marketing",
                },
                cb_kwargs={
                    "page_number": next_page_number,
                },
            )

    # def parse_subscribers(self, response: TextResponse):
    #     print("SUBSCRIBERS")
    #     x = response.xpath(
    #     "//vue[@name='subsite-details']
    #     /textarea/text()").get()
    #     xx = json.loads(x)
    #     print()
