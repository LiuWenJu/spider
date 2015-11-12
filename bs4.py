#coding=utf-8

from bs4 import BeautifulSoup
import requests


url = "http://www.yellowpages.com/los-angeles-ca/health-and-wellness"

r = requests.get(url)

soup = BeautifulSoup(r.content)

href = soup.find_all("href")
for item in href:
    print item
