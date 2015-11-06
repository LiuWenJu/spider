#coding=utf-8

import requests
import re
import urllib

proxy = {"http":"http://127.0.0.1:1080","https":"https://127.0.0.1:1080"}
#headers = { 'User-Agent': 'User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36' }

def getHtml(url):
    r = requests.get(url,proxies=proxy)
    html = r.text
    return html

def saveImg(html):
    reg = re.compile(r'img src="(.*?\.jpg)" onclick')
    imglist = re.findall(reg, html)
    print imglist

url = 'http://t66y.com/htm_data/7/1510/1700160.html'
ht = getHtml(url)
saveImg(ht)
