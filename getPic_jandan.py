#coding=utf-8

import re
import os
import urllib
import requests
from bs4 import BeautifulSoup

start_page = 1400
end_page = 1450

if not os.path.exists ('./jandan'):
        os.mkdir('./jandan')
        os.chdir('./jandan')

class Jandan(object):

    
    def __init__(self, url):
        self.url = url

    def gethtml(self, url):
        r = requests.get(url)
        html = r.text
        return html

    def getimg(self, html):
        reg = re.compile(r'src="(.*?\.jpg)" ')
        imglists = re.findall(reg, html)
        tireg = re.compile(r'title=.*?\>"(\s)"')
        tillist = re.findall(tireg, html)
        for img in imglists:
            for t in tillist:
                urllib.urlretieve(img, t.jpg)

    def url(self, start_page, end_page):
        urls = []
        for page in range(start_page, end_page):
            urls.append("http://jandan.net/ooxx/page-%d" % page)

if __name__ == "__main__":
    url = "http://jandan.net/ooxx/page-"
    a = Jandan(url)
    #a.url(1600,1606)
    s = a.gethtml(url)
    a.getimg(s)
    print s

