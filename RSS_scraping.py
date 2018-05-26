# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup


url  ="https://www.amazon.com.au/gp/rss/bestsellers/electronics"
resp = requests.get(url)
soup = BeautifulSoup(resp.content, features="xml")

# print soup.prettify()

item_name = []
item_description = []
item_price = []

for item in soup.find_all("item"):
    for title in item.find_all("title"):
        print title.text
    for description in item.find_all("description"):
        item_description.append(description)
        price = re.findall(r"(?:\£|\$|\€)(?:[\d\.\,]{1,})",description.text)

        if len(price) == 1:
            item_price.append(price[0])
        elif len(price) > 1:
            item_price.append(price[1])

print len(item_name)
print len(item_description)
print len(item_price)