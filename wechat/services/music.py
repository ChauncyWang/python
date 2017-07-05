import requests
from netease.weapi import Crawler
import os

import pygame,sys

c = Crawler()
a = c.search("十年", search_type=1, limit=1)
name = a['result']['songs'][0]['name']

a = c.get_song_url(a['result']['songs'][0]['id'])
a = requests.get(a)
with open("%s.mp3" % name, "wb") as code:
    code.write(a.content)

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode([640,480])
pygame.time.delay(1000)#等待1秒让mixer完成初始化
pygame.mixer.music.load("%s.mp3" % name)
pygame.mixer.music.play()
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()