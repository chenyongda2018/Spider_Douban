import requests
from bs4 import BeautifulSoup
import re
import pymongo

# 创建数据库连接
client = pymongo.MongoClient(host="localhost", port=27017, connect=False)

# 连接数据库
db = client['nishuihan']
# 验证用户
db.authenticate(name="syyyy", password="123456")
# 这里会在数据库中创建集合
dbSet = db['nsh_cbg']
# 这里指定以 第几列字段为索引，注意:此字段不允许出现重复，否则报错
# dbSet.create_index([("id", 1)], unique=True)

url = "https://n.cbg.163.com/?serverid=1"
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, "lxml")
columns = soup.select('tr[data-serverid="1"]')

# print(columns[0])
i = 0
for col in columns:
    i += 1
    good_name = col.select("p.goods-name")[0].get_text()  # 铜钱
    good_value = col.select("td")[1].select("p")[0].get_text()  # 面值
    good_name = good_name + good_value  # 物品完整名称 例:铜钱300万
    good_price = col.select("td.c_Red")[0].get_text()
    good_price = re.findall("\d+.?\d*", good_price)[0]  # 总价
    unit_price = col.select("td.c_Red")[1].get_text().strip()  # 单价
    buy_level = col.select("td")[4].get_text().strip()  # 交易登记
    sell_time = col.select("td")[6].get_text().strip()  # 购买剩余时间

    data = {
        "good_id": i,
        "name": good_name,
        "price": good_price,
        "unit_price": unit_price,
        "buy_level": buy_level,
        "sell_time": sell_time
    }
    # dbSet.insert_one(data)
    print(data)
