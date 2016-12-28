import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import numpy as np

def getNews():
    url = "https://news.google.co.in/news/section?cf=all&pz=1&ned=in&topic=w&siidp=2ffd7c5274d0209ca1a2ef21b3a0d18493b4&ict=ln"
    news_file = urllib2.urlopen(url)
    news_html = news_file.read()
    news_file.close()

    soup = BeautifulSoup(news_html, 'html.parser')

    title = soup.find_all('span', attrs={'class' : 'titletext'})

    topNews = []

    for i in title:
        topNews.append(i.text)

    print "\n\033[1mTop News\033[00m" + "\n"
    for i in topNews:
        print '\033[94m' + i + '\033[00m'

getNews()