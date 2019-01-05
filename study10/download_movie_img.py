# coding:utf-8
from selenium import webdriver
from lxml import etree
import time
import requests
import json


def download2(src, filename):
    directory = './download2/' + str(filename) + '.webp'
    try:
        pic = requests.get(src, timeout=10)
    except requests.exceptions.ConnectionError:
        # print 'error, %d 当前图片无法下载', %id
        print('图片无法下载')
    fp = open(directory, 'wb')
    fp.write(pic.content)
    fp.close()


query = "王祖贤"
# url = "https://movie.douban.com/subject_search?search_text=" + "&cat=1002&limit=15&start=" +75

cover_xpath = "//div[@class='item-root']//img[@class='cover']/@src"
description_xpath = "//div[@class='item-root']//img[@class='cover']/@alt"

webdriver_path = "C:/Users/Nansh/Downloads/chromedriver_win32/chromedriver.exe"
my_driver = webdriver.Chrome(executable_path=webdriver_path)

for index in range(0, 90, 15):
    url = "https://movie.douban.com/subject_search?search_text=" + query + "&cat=1002&limit=15&start=" + str(index)

    print(url)
    my_driver.get(url)
    time.sleep(1)
    html = etree.HTML(my_driver.page_source)
    covers = html.xpath(cover_xpath)
    descriptions = html.xpath(description_xpath)

    for img_url, title in zip(covers, descriptions):
        download2(img_url, title.replace("?", "_"))


my_driver.close()