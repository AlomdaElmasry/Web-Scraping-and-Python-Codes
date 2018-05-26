from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd


def getNews(u):
    news_file = urllib2.urlopen(u)
    news_html = news_file.read()
    news_file.close()

    soup = BeautifulSoup(news_html, "html.parser")

    title = soup.find_all("div", attrs={"class" : "post-title"})
    desc = soup.find_all("div", attrs={"class" : "post-description"})

    sequence = ["Title", "Description"]
    df = pd.DataFrame()
    df = df.reindex(columns=sequence)

    t = []
    for i in title:
        t.append(i.text)

    d = []
    for i in desc:
        d.append(i.text)

    t = map(lambda s: s.strip(), t)
    d = map(lambda s: s.strip(), d)

    df["Title"] = t
    df["Description"] = d

    print df

url = "https://sports.ndtv.com/cricket/news"
getNews(url)

