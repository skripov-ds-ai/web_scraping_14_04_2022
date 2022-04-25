from pprint import pprint

import requests

# pip install lxml
from lxml.html import fromstring


def get_first_elem_or_none(arr):
    # если непустой список
    if arr:
        return arr[0]
    return None


URL = "https://ru.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/98.0.4758.80 Safari/537.36",
}
ITEMS_XPATH = '//ul[contains(@class, "list__items")]/li'
TITLE_XPATH = './/*[contains(@class, "item__title")]'
IMG_XPATH = ".//img/@src"
PRICE_XPATH = './/span[contains(@class, "price")]//text()'

r = requests.get(URL, headers=HEADERS)
dom = fromstring(r.text)
items = dom.xpath(ITEMS_XPATH)
info_list = []

for item in items:
    info = {}
    # info['title'] = item.xpath(TITLE_XPATH)[0]
    info["title"] = get_first_elem_or_none(item.xpath(TITLE_XPATH))
    info["img"] = item.xpath(IMG_XPATH)[0]
    info["price"] = item.xpath(PRICE_XPATH)
    pprint(info)
    info_list.append(info)
    print()

print()


# ITEM_XPATH = '//ul[contains(@class, "srp-results")]/li'
# PART_OF_TITLE_XPATH = './/h3[@class="s-item__title"]//text()'
# PART_OF_LINK_TO_ITEM_FROM_TITLE_XPATH = "./parent::a/@href"
# IMG_ALT_XPATH = ".//img/@alt"
# IMG_SRC_XPATH = ".//img/@src"
# PART_OF_PRICE_XPATH = './/span[contains(@class, "s-item__price")]'
# AUCTION_PRICE_XPATH = ".//text()"
# # PART_OF_LINK_TO_ITEM_FROM_TITLE_XPATH = "/parent::*/@href" ?
#
# response = requests.get(URL, headers=HEADERS)
# dom = fromstring(response.text)
# print()
#
# items = dom.xpath(ITEM_XPATH)
# item_infos = []
# for item in items:
#     info = {}
#     info["url"] = item.xpath(PART_OF_LINK_TO_ITEM_FROM_TITLE_XPATH)[0]
#     info["title"] = item.xpath(PART_OF_TITLE_XPATH)[0]
#     info["prices"] = list(
#         map(
#             lambda x: " ".join(x.xpath(AUCTION_PRICE_XPATH)),
#             item.xpath(PART_OF_PRICE_XPATH),
#         )
#     )
#     info["img_alt"] = item.xpath(IMG_ALT_XPATH)[0]
#     info["img"] = item.xpath(IMG_SRC_XPATH)[0]
#
#     print()
# pprint(items)


# from fp.fp import FreeProxy
# from lxml.html import fromstring
#
# FP_OBJECT = FreeProxy()
#
#
# def get_proxies():
#     return FP_OBJECT.get_proxy_list()
#
#
# def retry_request(url, headers, proxy_list, retry_number=3):
#     if len(proxy_list) == 0:
#         # TODO: what should be character of this function?
#         print("proxy_list is empty")
#         return None
#
#     for i, proxy_string in enumerate(proxy_list):
#         if i > retry_number:
#             return None
#         try:
#             proxy = {"http": proxy_string}
#             response = requests.get(url, headers=headers, proxies=proxy)
#             response.raise_for_status()
#             if response.status_code == 200:
#                 return response
#         except Exception as e:
#             print(e)
#             print(f"Exception on {i}-th retry on {url}")
#     return None
#
#
# def process_item(item):
#     img_xpath = ".//img/@src"
#     title_xpath = './/h3[contains(@class, "_title")]/text()'
#     price_xpath = './/*[contains(@class, "_price")]//text()'
#     info = {}
#     try:
#         info["title"] = item.xpath(title_xpath)[0]
#     except Exception as e:
#         print(e)
#         # TODO: fix type of exception
#         raise Exception(f"Cannot extract title from item: {item}")
#     info["price"] = item.xpath(price_xpath)
#     info["img"] = item.xpath(img_xpath)
#     return info
#
#
# def process_items(items):
#     items_info = []
#     for item in items:
#         try:
#             info = process_item(item)
#             items_info.append(info)
#         except Exception as e:
#             print(e)
#     return items_info
#
#
# def ebay_pipeline(url, headers, proxy_list, retry_number=3):
#     response = retry_request(url, headers, proxy_list, retry_number)
#     # if response is None
#     if not response:
#         return
#
#     dom = fromstring(response.text)
#     items_xpath = (
#         '//ul[contains(@class, "-results")]'
#         '//div[contains(@class, "s-item__wrapper")]'
#     )
#     items = dom.xpath(items_xpath)
#     items_info = process_items(items)
#     pprint(items_info)
#     print()
#     # TODO: saving...
#
#
# url = (
#     "https://www.ebay.com/sch/i.html?_nkw=Sunglasses&_sacat=79720"
#     "&_trkparms=pageci%3Ae4180a30-e0c2-11eb-85a5-46b77bf42edf%7C"
#     "parentrq%3A8bb1c7df17a0acf3822a4a0affda7f56%7Ciid%3"
# )
# headers = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
#                   "(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
# }
# proxy_list = get_proxies()
# retry_number = 2
# ebay_pipeline(url, headers, proxy_list, retry_number)
#
#
# # response = requests.get(url, headers=headers)
# # dom = fromstring(response.text)
# # print()
# #
# # img_xpath = './/img/@src'
# # title_xpath = './/h3[contains(@class, "_title")]/text()'
# # price_xpath = './/*[contains(@class, "_price")]//text()'
# # items_xpath = '//ul[contains(@class, "-results")]//
# # div[contains(@class, "s-item__wrapper")]'
# # items_info = []
# # for item in dom.xpath(items_xpath):
# #     info = {}
# #     try:
# #         info['title'] = item.xpath(title_xpath)[0]
# #     except Exception as e:
# #         print(e)
# #         continue
# #     info['price'] = item.xpath(price_xpath)
# #     info['img'] = item.xpath(img_xpath)
# #     items_info.append(info)
# #     pprint(info)
# # print()
