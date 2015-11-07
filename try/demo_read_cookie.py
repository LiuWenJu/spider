#coding=utf-8
import cookielib
import urllib2

cookie = cookielib.MozillaCookieJar()
#创建MozillaCookieJar实例对象

cookie.load('cookie.txt', ignore_discard = True, ignore_expires=True)
#从文件中读取cookie的内容到变量

req = urllib2.Request("http://www.baidu.com")
#创建请求的request

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#利用urllib2的build_opener方法创建一个opener
response = opener.open(req)
print response.read()
