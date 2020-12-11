import requests
from lxml import etree


url = "https://www.wuxiaworld.com/page/general-glossary-of-terms"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

response = requests.get(url, headers= headers).text
# print(response)
dom=etree.HTML(response)
texts = dom.xpath('//')