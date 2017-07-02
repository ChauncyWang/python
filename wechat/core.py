import requests
from wechat.services.login import *
class Core:
    def __init__(self):
        self.session = requests.session()
