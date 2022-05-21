# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline


class LabirintPipeline:
    def process_item(self, item, spider):
        print("PROCESS_ITEM")
        print()
        # TODO: write code for MongoDB
        return item


class LabirintImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        img_urls = []
        img_urls.extend(item["img_urls"])
        print()
        if item["main_img_url"]:
            img_urls.append(item["main_img_url"])
        print()
        img_urls = set(img_urls)
        print()

        if img_urls:
            for img_url in img_urls:
                try:
                    yield Request(img_url)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        print("ITEM_COMPLETED")
        print()
        if results:
            item["img_info"] = [r[1] for r in results if r[0]]
            del item["img_urls"]
            del item["main_img_url"]
        print()
        return item
