import pymongo
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

client = pymongo.MongoClient(host="localhost", port=27017)
# client = MongoClient('mongodb://localhost:27017/')
db = client['douban']

# 获取数据库中的集合
collections = db['douban_tv']


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        results = collections.find({})
        self.render("douban_us_tv.html", records=results)


class DelHandler(tornado.web.RequestHandler):
    def get(self, id=None):
        if id:
            movie = collections.delete_one({'id': id})
        self.redirect("/douban")

handlers = [
    (r"/douban", IndexHandler),
    (r"/douban/delete/([0-9Xx\-]+)", DelHandler)
]
# 获取存放模板的 template 路径
template_path = os.path.join(os.path.dirname(__file__), "douban_us_web")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    # debug = True 时,我们修改了代码不用重启Tornado就可以看效果
    app = tornado.web.Application(handlers, template_path, debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
