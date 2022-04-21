from pprint import pprint

# pip install bson pymongo
from bson import ObjectId
from pymongo import ASCENDING, DESCENDING, MongoClient


MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "posts"
MONGO_COLLECTION = "news"
# d = dict(a=1)
# something like
# URI = "mongodb://localhost:port@username:password"

# client = MongoClient(MONGO_HOST, MONGO_PORT)
# # client = MongoClient(URI)
# ...
# client.close()
#
# with MongoClient(MONGO_HOST, MONGO_PORT) as client:
#     pass


def print_mongo_docs(cursor):
    for doc in cursor:
        pprint(doc)


# CRUD
# 1. Create - INSERT?
# 2. Read - SELECT?
# 3. Update - UPDATE?
# 4. Delete - DELETE?


with MongoClient(MONGO_HOST, MONGO_PORT) as client:
    # мы хотим добраться до posts
    # db = client.posts
    # db = client["posts"]
    db = client[MONGO_DB]
    # collection = db.news
    collection = db[MONGO_COLLECTION]

    # 4. Delete
    # удаляем коллекцию с данными внутри
    # db.drop_collection(MONGO_COLLECTION)
    # удаление коллекции(но коллекция существует пока
    # там есть хотя бы 1 документ!)
    # collection.drop()

    # 1. Create - INSERT
    doc = {
        "title": "Biden win elections",
        "rating": 100.99,
        "number_of_comments": 4,
    }
    # collection.insert_one(doc)

    # этот _id уже существует в БД
    # oid = "62619500dcd90eaaf0f53dbc"
    # doc_for_exception = {
    #     "_id": ObjectId(oid),
    #     "title": "Warren Buffet buys something"
    # }
    # collection.insert_one(doc_for_exception)

    docs = [
        {
            "title": "Buffet buys stocks",
            "rating": -79,
            # ? find for embedded list?
            "comments": ["It's wonderful!"],
        },
        {
            "title": "Charlie Munger also buy stocks",
            "rating": 0,
        },
    ]
    docs1 = [
        {
            "title": "ABC",
            "reactions": {
                "like": {"count": 101},
                "shares": {
                    "count": 0,
                },
            },
        },
        {
            "title": "BCA",
            "reactions": {
                "like": {"count": 7},
                "shares": {
                    "count": 5,
                },
            },
        },
    ]
    # collection.insert_many(docs)
    # collection.insert_many(docs1)

    # 2. Read
    # вы получаете итератор, чтобы не загружать память
    # found_docs = collection.find()
    found_docs = list(collection.find())
    found_docs1 = list(collection.find({}))
    # cursor = collection.find()
    # print_mongo_docs(cursor)

    # exact matching
    # cursor = collection.find({
    #     "title": "Buffet buys stocks"
    # })
    # print_mongo_docs(cursor)
    # cursor = collection.find({
    #     "title": "Buffet buys stocks",
    #     "rating": -79,
    # })
    # print_mongo_docs(cursor)

    # rating > -1
    # cursor = collection.find({
    #     "rating": {"$gt": -1}
    # })
    # print_mongo_docs(cursor)
    # cursor = collection.find({
    #     "rating": {"$gt": -1}
    # }).sort("rating", ASCENDING)
    # cursor = collection.find({
    #     "rating": {"$gt": -1}
    # }).sort("rating", direction=ASCENDING)

    # $gt - > , $lt - <,  $gte - >= , $lte - <=
    # $ne - != , $eq - ==
    cursor = collection.find({"rating": {"$gt": -1}}).sort(
        [
            ("rating", ASCENDING),
            ("title", DESCENDING),
        ]
    )
    #
    # TOP_N = 3
    # cursor = cursor.limit(TOP_N)
    # print_mongo_docs(cursor)

    # $in
    cursor = collection.find({"rating": {"$in": [0, -79]}})
    print_mongo_docs(cursor)

    # TODO: pycharm presentation assistant
    # $and, $or
    cursor = collection.find(
        {
            "$or": [{"title": "Buffet buys stocks"}, {"rating": {"$gte": 0}}],
            # для примера
            # "number_of_comments": {"$gt": 0}
        }
    )
    print_mongo_docs(cursor)

    # $not - https://docs.mongodb.com/manual/reference/operator/query/not/
    # $nor - https://docs.mongodb.com/manual/reference/operator/query/nor/
    cursor = collection.find({"rating": {"$not": {"$lt": 0}}})
    print_mongo_docs(cursor)

    # вложенные(embedded) документы
    cursor = collection.find({"reactions.like.count": {"$lt": 999}})
    print_mongo_docs(cursor)

    # существование поля у объектов - $exists
    cursor = collection.find(
        {
            "rating": {
                "$exists": False,
            }
        }
    )
    cursor = collection.find(
        {
            "rating": {
                "$exists": True,
            }
        }
    )
    print_mongo_docs(cursor)

    # более сложный поиск и вычисление статистик:
    # aggregation

    # 3. Update
    # заменяет 1 объект!
    # если их несколько - первый попавшийся
    # replace замещает
    collection.replace_one(
        {
            "rating": 0,
        },
        {"a": "Hurrah!"},
    )
    print_mongo_docs(collection.find({"rating": 0}))
    print_mongo_docs(collection.find({"a": "Hurrah!"}))

    # обновляет значение поля,
    # добавляет поле или убирает по запросу
    collection.update_one(
        {
            "_id": ObjectId("626197e9eebfc67e92c61e78")
            # "rating": 0,
        },
        {
            "$set": {
                "rating": 1,
                # "title": "Not Charlie",
            },
            "$unset": {
                "title": None,
            },
        },
    )
    cursor = collection.find({"_id": ObjectId("626197e9eebfc67e92c61e78")})
    print_mongo_docs(cursor)

    collection.update_many(
        {"rating": {"$gt": 99}},
        {
            "$inc": {
                # +3
                "rating": 3,
                # -2.9
                # "rating": -2.9,
            }
        },
    )
    cursor = collection.find(
        {
            "rating": {"$gt": 99},
        }
    )
    print_mongo_docs(cursor)

    # UPSERT
    # ?
    collection.update_one({"rating": -999}, {"$set": {"title": "New title!"}})
    cursor = collection.find({"rating": -999})
    print_mongo_docs(cursor)

    # true UPSERT
    collection.update_one(
        {"rating": -999},
        {"$set": {"title": "New title!"}},
        upsert=True,
    )
    cursor = collection.find({"rating": -999})
    print_mongo_docs(cursor)

    # 4. Delete
    # Danger!
    # collection.delete_one({})
    # удаляем все документы
    # collection.delete_many()
    collection.delete_many({"rating": 103.99})
    cursor = collection.find(
        {
            "rating": {"$gt": 99},
        }
    )
    print_mongo_docs(cursor)
    print()


# with MongoClient(MONGO_HOST, MONGO_PORT) as client:
#     # posts
#     # db = client.posts
#     # db = client['posts']
#     db = client[MONGO_DB]
#
#     # collection = db.social_network_posts
#     # MONGO_COLLECTION_NEW
#     collection = db[MONGO_COLLECTION_NEW]
#
#     # 4. Delete for collection/database
#     # delete all documents of current collection
#     # collection.drop()
#     # delete collection with name
#     # db.drop_collection(MONGO_COLLECTION_NEW)
#
#     # 1. Create
#     post_doc = {
#         "title": "Something with Biden",
#         "rating": 70,
#         "count_of_comments": 4,
#     }
#     post_doc_0 = {
#         "title": "Something with Biden",
#         "rating": -1,
#         "count_of_comments": 4,
#     }
#     post_doc_1 = {"title": "Trump elections"}
#     # collection.insert_one(post_doc_0)
#     # collection.insert_one(post_doc)
#     # collection.insert_many([post_doc, post_doc_1])
#     # print()
#
#     # 2. Read
#     # cursor = collection.find()
#     # cursor = collection.find({})
#     # exact matching
#     # cursor = collection.find({
#     #     # "title": "Trump elections",
#     #     "title": "Something with Biden",
#     # })
#     # cursor = collection.find({
#     #     # "title": "Trump elections",
#     #     "title": "Something with Biden",
#     # }).limit(3)
#     # cursor = collection.find({
#     #     # "title": "Trump elections",
#     #     "title": "Something with Biden",
#     # }).sort("rating", direction=ASCENDING).limit(3)
#     # multiple key sorting
#     cursor = collection.find(
#         {
#             # "title": "Trump elections",
#             "title": "Something with Biden",
#         }
#     ).sort(
#         [
#             ("rating", ASCENDING),
#             ("count_of_comments", DESCENDING),
#         ]
#     )
#     # cursor = collection.find({
#     #     "title": {"$eq": "Trump elections"}
#     # })
#     # cursor = collection.find({
#     #     "title": {"$ne": "Trump elections"}
#     # })
#     # $gt - > ; $gte - >= ; $lt - < ; $lte - <=
#     # cursor = collection.find({
#     #     "rating": {"$gt": 0},
#     #     "count_of_comments": 4,
#     # })
#     # $and ; $or ; $not - logic operations
#     # cursor = collection.find({
#     #     # $and
#     #     "$or": [
#     #         {
#     #             "rating": {"$lt": 0}
#     #         },
#     #         {
#     #             "rating": {"$eq": 0}
#     #         }
#     #     ]
#     # })
#     # $not - https://docs.mongodb.com/manual/reference/operator/query/not/
#     # $nor - https://docs.mongodb.com/manual/reference/operator/query/nor/
#     cursor = collection.find({"rating": {"$not": {"$lt": 0}}})
#     # print_mongo_docs(cursor)
#     # $in
#     cursor = collection.find(
#         {
#             # filter!
#             "rating": {"$in": [-1, 1]}
#         }
#     )
#     # regex
#     # https://docs.mongodb.com/manual/reference/operator/query/regex/
#     # print("=" * 15)
#     # print_mongo_docs(cursor)
#     # если данных немного, то можно считать их все в RAM
#     # retrieved_data = list(cursor)
#
#     # 3. Update
#     collection.update_one(
#         {"_id": ObjectId("620a8bb4e4dafa81d06d8ab1")},
#         {
#             "$set": {
#                 "title": "not Biden",
#                 "rating_1": 90,
#             },
#             "$unset": {
#                 "rating": None,
#             },
#         },
#     )
#     # title1 -> title1_1 ; title2 -> title2_1 - not this way
#     # title1 -> titleX ; title2 -> titleX
#     # collection.update_many(
#     #     {
#     #         # "rating": 70,
#     #         "rating": 71,
#     #     },
#     #     {
#     #         # "$inc": {"rating": 1},
#     #         "$inc": {"rating": -1},
#     #     }
#     # )
#     #
#     # UPSERT
#     collection.update_one(
#         {
#             "rating": 60,
#         },
#         {
#             "$set": {
#                 "title": "no",
#                 "rating_1": 99,
#             },
#         },
#         upsert=True,
#     )
#     collection.replace_one(
#         {
#             "rating": 60,
#         },
#         {
#             "title": "no",
#             "rating_1": 99,
#         },
#     )
#
#     cursor = collection.find(
#         {
#             "rating": 60,
#         },
#     )
#     print_mongo_docs(cursor)
#
#     # 4. Delete
#     # ?
#     # collection.delete_one({})
#     # collection.delete_many()
#     #
#     collection.delete_one(
#         {
#             "title": "no",
#             "rating_1": 99,
#         }
#     )
#     collection.delete_many(
#         {
#             "rating": {"$gt": 0},
#         }
#     )
