import pymongo

client = pymongo.MongoClient(host="localhost", port=27017)
# client = MongoClient('mongodb://localhost:27017/')
db = client['douban']

# 获取数据库中的集合
collections = db['douban_tv']

results = collections.find({'rate': '9.2'})

for result in results:
    print(result['title']+" "+result['img_url'])