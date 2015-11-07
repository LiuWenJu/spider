#coding=utf-8

import urllib2
#import re


url = 'http://jandan.net/ooxx'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response
