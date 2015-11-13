#coding=utf-8

from bs4 import BeautifulSoup
import requests

url = "http://www.amazon.cn/gp/bestsellers/books/ref=s9_acsd_ri_bw_clnk?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=merchandised-search-5&pf_rd_r=0Y1F0E7MATQPWDH0MMD0&pf_rd_t=101&pf_rd_p=261616452&pf_rd_i=658390051_p0_h"

r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

href = soup.find_all("a")
for item in href:
    print item.text, item.get("href")
