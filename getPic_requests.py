#coding=utf-8

import requests
import re
import urllib
import os

if os.path.exists("/home/liuwj/spider/img"):
    os.chdir('img')
else:
    os.mkdir('img')
    os.chdir('img')

print "*" * 15
print "保存图片中,按CTRL+C停止"
print
print "*" * 15


def html(url):
    r = requests.get(url)
    html = r.text
    return html


def saveImg(html):
    reg = re.compile(r'src="(.*?\.jpg)" pic_ext')
    imglist = re.findall(reg, html)

    x = 1
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s_%s.jpg' % (page, x))
        x += 1

page = 21
while page < 36:
    url = "http://tieba.baidu.com/p/3956908596?pn="+str(page)
    page +=1
    ht = html(url)
    saveImg(ht)
    print "现在保存了下列的图片:"
    os.system('ls')
    print "等不及看图片?按CTRL+C停止"

print "congratulations!图片保存完成!"

