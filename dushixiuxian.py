# -*- coding: utf-8 -*-

import requests
from lxml import etree
from bs4 import BeautifulSoup
import time

base_url = 'https://www.zhuaji.org/read/26034/' 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

response = requests.get(url = base_url, headers = headers)
result=response.text
# print(result)
dom = etree.HTML(result)
novel_urls = dom.xpath('//dd/a[@href]/@href')
novel_names = dom.xpath('//dd/a/text()')
# print(novel_names)
# print(novel_urls)
for novel_url, novel_name in zip(novel_urls,novel_names):
    # print(novel_name)
    # print(novel_url)
    real_url = 'https://www.zhuaji.org'+format(novel_url)
    # print(real_url)
    res = requests.get(url = real_url, headers = headers, verify= False)

    html = res.text
    soup = BeautifulSoup(html, "lxml")
    r = soup.find("div", id = "content")
    texts = r.text.replace('\xa0'*4, '\n\n')
    
    # print(texts)

    with open(r'D:\APPS\Microsoft VS Code\works\xiuxian./%s.txt'%novel_name, 'w') as file:
        file.write(texts)
        time.sleep(15)

