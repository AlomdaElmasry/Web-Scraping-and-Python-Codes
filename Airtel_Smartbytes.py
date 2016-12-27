import urllib2
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def getData():
    url = "http://122.160.230.125:8080/planupdate/"
    data_file = urllib2.urlopen(url)
    data_html = data_file.read()
    data_file.close()

    data = []

    soup = BeautifulSoup(data_html, 'html.parser')

    main = soup.find_all("div", attrs={'class': 'description'})

    for i in main:
        for j in i.find_all('span'):
            data.append(j.text)

    print "\nYour monthly high-speed data limit is : " + str(data[0])
    print "You are left with : " + str(data[1])
    print "No. of days left in the current bill cycle : " + str(data[2])
    print "DSL Number : " + str(data[3])

getData()