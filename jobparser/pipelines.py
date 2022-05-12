# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient

MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "jobs"


# вариант получше здесь -
# https://docs.scrapy.org/en/latest/topics/
# item-pipeline.html#write-items-to-mongodb
class JobparserPipeline:
    def __init__(self):
        self.client = MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.client[MONGO_DB]

    def process_salary(self, salary_list: list):
        # TODO
        return None, None, "RUB"

    def process_item(self, item, spider):
        # print("PIPELINE")
        s_min, s_max, s_currency = self.process_salary(item["salary"])
        item["title"] = " ".join(item["title"])
        if s_min:
            item["salary_min"] = s_min
        item["salary_max"] = s_max
        item["salary_currency"] = s_currency
        # del item['salary']
        item.pop("salary")

        collection = self.db[spider.name]
        # print()
        collection.insert_one(item)
        # update_one upsert

        # print()
        return item
