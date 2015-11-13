#coding=utf-8

from bs4 import BeautifulSoup
import requests

url = "http://www.yellowpages.com/atlanta-ga/fire-water-damage-restoration"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

links = soup.find_all("a")
for	item in links:
    print "<a href='%s'>%s</a>" %(item.get("href"), item.text)


data = soup.find_all("div", {"class": "info"})

list = []
for item in data:
    try:
        l1 = item.contents[0].find_all("a", {"class": "business-name"})[0].text + "\n"
        list.append(l1)
        print l1
    except:
        print "l1 error"

        #with open('test.txt','a+') as f:
        #    f.writelines(l1)

    try:
        l2 = item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text + "\n"
        print l2
        list.append(l2)
    except:
        print "l2 error"

#        with open('test.txt','a+') as f:
#            f.writelines(l2)

    try:
        l3 = item.contents[1].find_all("div", {"itemprop": "telephone"})[0].text + "\n"
        print l3
        list.append(l3)
    except:
        print "l3 error"

#        with open('test.txt','a+') as f:
#            f.writelines(l3)
    try:
        l4 = item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text + "\n"
        print l4
        list.append(l4)
    except:
        print "l4 error"
#        with open('test.txt','a+') as f:
#            f.writelines(l4)
with open('list.txt', 'w+') as file:
    for l in list:
        file.writelines(l)

