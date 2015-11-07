#coding=utf-8

import urllib
import urllib2
import cookielib
import re


class SDU:

    def __init__(self):
        self.loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
        self.gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bskcjcx.curscopre'
        self.cookies = cookielib.CookJar()
        self.postdata = urllib.urlencode({
            'stuid':'201200131012',
            'pwd':'000000'
        })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        self.credit = []
        self.grades = []

    def getPage(self):
        request = urllib2.Request(
            url = self.loginUrl,
            data = self.postdata
        )
        result = self.opener.open(request)
        result = self.opener.open(self.gradeUrl)
        return result.read().decode('gbk')

    def getGrade(self):
        page = self.getPage()
        myItems = re.findall('<TR>.*?<p.*?<p.*?<p.*?<p.*?<p.*?>(.*?)</p>.*?<p.*?<p.*?>(.*?)</p>.*?</TR>',page,re.S)
        for item in myItems:
            self.credit.append(item[0].encode('gbk'))
            self.grades.append(item[1].encode('gbk'))
        self.getGrade()

    def getGrade(self):
        sum = 0.0
        weight = 0.0
        for i in range(len(self.credit)):
            if(self.grades[i].isdeigit()):
                sum += string.atof(self.credit[i])*string.atof(self.grades[i])
                weight += string.atof(self.credit[i])
        print u"The socres of this team",sum/weight


sdu =SDU()
sdu.getGrades()
