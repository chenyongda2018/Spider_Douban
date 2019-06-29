import requests
import pymongo
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

# 创建数据库连接
client = pymongo.MongoClient(host="localhost", port=27017, connect=False)

# 连接数据库
db = client['nishuihan']
# 验证用户
db.authenticate(name="syyyy", password="123456")
# 这里会在数据库中创建集合
dbSet = db['nsh_cbg']


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        goodlist = dbSet.find({})
        self.render("nsh.html", goods=goodlist)


class DelHandler(tornado.web.RequestHandler):
    def get(self, good_id=None):
        if good_id:
            good = dbSet.delete_one({'good_id': good_id})
        self.redirect("/nsh")


handlers = [
    (r"/nsh", IndexHandler),
    (r"/nsh/del/([0-9Xx\-]+)", DelHandler)
]
# 获取存放模板的 template 路径
template_path = os.path.join(os.path.dirname(__file__), "spider_nishuihan")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    # debug = True 时,我们修改了代码不用重启Tornado就可以看效果
    app = tornado.web.Application(handlers, template_path, debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
