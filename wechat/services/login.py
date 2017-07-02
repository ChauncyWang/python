import io
import re

import pyqrcode
from itchat.config import USER_AGENT

import wechat
from wechat.config import WX_URL


def getQRuuid():
    url = '%s/jslogin' % WX_URL
    params = {
        'appid': 'wx782c26e4c19acffb',
        'fun': 'new'
    }
    headers = {
        'User-Agent': USER_AGENT
    }

    response = wechat.session.get(url, params=params, headers=headers)
    regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)";'
    data = re.match(regx, response.text)

    if data and data.group(1) == '200':
        return data.group(2)

def getQR(uuid):
    url = 'https://login.weixin.qq.com/l/%s' % uuid
    qr = pyqrcode.QRCode(url)
    print(qr.text(1).replace('0', "  ").replace('1', u'\u2588\u2588'))
    return 0
