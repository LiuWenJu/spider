#coding=utf-8

import urllib
import re
from bs4 import BeautifulSoup

#帖子数量0/50/100/150
pn = "0"
baseUrl = "http://tieba.baidu.com/f?ie=utf-8&kw=bilibili&pn="


class main(object):

    def __init__(self, baseUrl, pn):
        self.baseUrl = baseUrl
        self.pn = pn
        self.user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"

    def getHtml(self):
        try:
            url = self.baseUrl+self.pn
            req = urllib.request.Request(url)
            req.add_header('User-Agent',"self.user_agent")
            with urllib.request.urlopen(req) as f:
                data = f.read().decode('utf-8', 'ignore')
        except Exception, e:
            if hasattr(e,"code"):
                print (e.code)
            if hasattr(e,"reason"):
                print (e.reason)
        return data

    def tool(self,data):
        soup = BeautifulSoup(data, "html5ib")
        #
        rep_num = soup.find_all("span",class_="threadlist_rep_num center_text")
        #
        title = soup.find_all("a",class_="j_th_tit ")
        #
        author = soup.find_all("span",class_="tb_icon_author")
        #
        time = soup.find_all("span",class_="pull-right is_show_create_time")
        #
        content = soup.find_all("div",class_="threadlist_abs threadlist_abs_onlyline ")
        contents = ""
        for i in range(47):
            contents = contents+"------------------"+title[i].string.strip()+"---------------\n"
            contents = contents + author[i]['title'].strip()+"\n"
            if content[i] and i>1:
                contents = contents + content[i].string.strip()+"\n"
            else:
                content = "图\n"
            contents = contents+"---------"+"时间: "+time[i].string.strip()+"------"+rep_num[i].string+"-------\n\n"
            return contents

i = main(baseUrl,pn)
print (i.tool(i.getHtml()))
