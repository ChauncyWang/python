import sys
import web

sys.path.append("/home/wx")
from wechat.oa.handle import Handle

urls = (
    '/', 'Handle'
    '/index.html', 'Handle'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
