import requests
from lxml import etree

r = requests.get('http://www.douban.com')

text = r.text
content = r.content

html = etree.HTML(text)
result = html.xpath('//li')

pic_xpath = "//div[@class='result-list']/div[@class='result']//a[@class='nbg']/img/@src"
