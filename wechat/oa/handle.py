import time

import web

from wechat.oa import *
from wechat.oa.receive import parse_xml_msg

render = web.template.render("/home/wx/wechat/oa/templates/")


class Handle:
    def GET(self, name=None):
        print(name)
        if name is None:
            try:
                web_input = web.input()
                return validate_token(web_input)
            except Exception as Argument:
                print(Argument)
                return Argument
        else:
            print(name)
            web.redirect("/static/%s" % name)

    def POST(self):
        try:
            web_data = web.data()
            r = parse_xml_msg(web_data)
            print(r.FromUserName, "->", r.ToUserName, ":", r.Content)
            r = render.re_msg_text(r.FromUserName, r.ToUserName, int(time.time()), r.Content)
            return r
        except Exception as Argment:
            print(Argment)
            return Argment
