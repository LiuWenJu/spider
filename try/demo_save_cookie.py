#coding=utf-8
import cookielib
import urllib2

filename = 'cookie.txt'
#设置保存cookie的文件,同级目录下的cookie.txt

cookie = cookielib.MozillaCookieJar(filename)
#声明一个MozillaCookieJar对象实例来保存cookie,之后写入文件

handler = urllib2.HTTPCookieProcessor(cookie)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器

opener = urllib2.build_opener(handler)
#通过handler来构建opener

response = opener.open("http://www.baidu.com")
#创建一个请求,原理同urllib2的urlopen

cookie.save(ignore_discard = True, ignore_expires = True)
#保存cookie到文件

