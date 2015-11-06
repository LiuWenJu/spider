#coding=utf-8

import urllib
import re
import os


def getSourse(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getJpg(html):
    reg = r'src="(.*?\.jpg)" pic_ext'
    img = re.compile(reg)
    imglist = re.findall(img, html)

    x = 1

    for i in imglist:
        if os.path.exists('/home/liuwj/spider/picture'):
            os.chdir('/home/liuwj/spider/picture')
        else:
            os.mkdir('picture')
            os.chdir('picture')

        urllib.urlretrieve(i, '%s.jpg' % x)
        x += 1

url = "http://tieba.baidu.com/p/2538090959"
html = getSourse(url)
getJpg(html)
