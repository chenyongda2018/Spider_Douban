#!/usr/bin/env python
# coding:utf-8

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options


'''
简单的表单提交示例
'''
define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


# 处理数据的Handler
class UserHandler(tornado.web.RequestHandler):
    def post(self):
        # 通过 self.get_argument("属性值")获得表单页面的数据,与<input> 中的 name值相同
        user_name = self.get_argument("username")
        user_email = self.get_argument("email")
        user_website = self.get_argument("website")
        user_language = self.get_argument("language")
        self.render("user.html", username=user_name, email=user_email, website=user_website, language=user_language)


handlers = [
    (r"/", IndexHandler),
    (r"/user", UserHandler)
]
# 获取存放模板的 template 路径
template_path = os.path.join(os.path.dirname(__file__), "template")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers, template_path)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
