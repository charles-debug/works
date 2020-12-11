from pyquery import PyQuery as pq
import requests
r = requests.get('http://www.cuiqingcai.com')
doc = pq(r.text)
print(doc('title'))