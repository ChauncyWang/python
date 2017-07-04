import re

import pyqrcode
import time

import wechat
from wechat import config

from xml.dom.minidom import parseString as ps

class Login:
    """
    登录类，登录的相关操作
    """

    def __init__(self):
        self.uuid = None
        self.redirect_uri = None
        self.session = wechat.session

    def login(self):
        """
        登录
        :return:
        """
        self.get_qr_uuid()
        print("请扫描下方二维码")
        self.show_qr()
        while True:
            t = self.check_login()
            if t == 200:
                self.get_login_info()
                break
            elif t == 201:
                print("扫描成功，请在手机上确认登录!")
            elif t == 400:
                raise Exception("未知错误!")


    def get_qr_uuid(self):
        """
        获取 qr 的 uuid
        :return: uuid
        """
        params = {
            'appid': 'wx782c26e4c19acffb',
            'fun': 'new'
        }
        headers = {
            'User-Agent': config.USER_AGENT
        }

        response = self.session.get(config.API_jsLogin, params=params, headers=headers)
        regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)";'
        data = re.match(regx, response.text)

        if data and data.group(1) == '200':
            self.uuid = data.group(2)

    def show_qr(self):
        """
        根据 uuid 直接显示二维码
        :param uuid:
        :return:
        """
        url = 'https://login.weixin.qq.com/l/%s' % self.uuid
        qr = pyqrcode.QRCode(url)
        print(qr.text(1).replace('0', u'\u2588\u2588').replace('1', "  "))
        return 0

    def check_login(self):
        """
        检查登录状态
        :param uuid: qr 的 uuid
        :return: 登录状态码
        """
        t = int(time.time())
        params = 'loginicon=true&uuid=%s&tip=0&_=%s' % (
            self.uuid, t)
        headers = {'User-Agent': config.USER_AGENT}
        r = self.session.get(config.API_login, params=params, headers=headers)
        regex = r'window.code=(\d+)'
        data = re.search(regex, r.text)

        if data and data.group(1) == '200':
            regex = r'window.redirect_uri="(.*?)"'
            data = re.search(regex, r.text)
            if data and data.group(1):
                self.redirect_uri = data.group(1)
                return 200
            else:
                return 400
        elif data:
            return int(data.group(1))
        else:
            return 400

    def get_login_info(self):
        url = self.redirect_uri
        r = self.session.get(url,)
        r = ps(r.text)
        r = r.documentElement
        print(r)