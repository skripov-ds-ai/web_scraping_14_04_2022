# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import scrapy

# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline


class OtparserPipeline:
    def process_item(self, item, spider):
        print("PROCESS_ITEM")
        print()
        # TODO: write code for MongoDB
        return item


class OtparserImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item["img_urls"]:
            for img_url in item["img_urls"]:
                try:
                    yield scrapy.Request(img_url)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        print("ITEM_COMPLETED")
        print()
        if results:
            item["img_info"] = [r[1] for r in results if r[0]]
            del item["img_urls"]
        return item
