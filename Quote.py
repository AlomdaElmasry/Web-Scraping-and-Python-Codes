from bs4 import BeautifulSoup
import urllib2
import random


def get_quote():
    url = "https://www.goodreads.com/quotes"

    quote_file = urllib2.urlopen(url)
    quote_html = quote_file.read()
    quote_file.close()

    soup = BeautifulSoup(quote_html, "html.parser")

    dic = {}

    for quote_data in soup.find_all("div", attrs={"id" : "quoteoftheday"}):
        for quote_text in quote_data.find_all("div", attrs={"class":"stacked mediumText"}):
            for i in quote_text.find_all("i"):
                dic["Quote"] = i.text

    for quote_data in soup.find_all("div", attrs={"id" : "quoteoftheday"}):
        for quote_author in quote_data.find_all("div", attrs={"class":"textRight"}):
            for st in quote_author.find_all("strong", attrs={"class":"mediumText"}):
                for a in st.find_all("a"):
                    dic["Authore"] = a.text

    print dic


get_quote()
