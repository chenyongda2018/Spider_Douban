import pymongo
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

# client = pymongo.MongoClient(host="localhost", port=27017)
# # client = MongoClient('mongodb://localhost:27017/')
# db = client['douban']
#
# # 获取数据库中的集合
# collections = db['douban_tv']
#
# results = collections.find({'rate': '9.2'})
#
# for result in results:
#     print(result['title']+" "+result['img_url'])