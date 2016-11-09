import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import numpy as np

# Stats Type List
t = ["Repositories", "Stars", "Followers", "Following"]

type = np.array(t)
l = []

def Get_Details():

    #Get Username
    x = raw_input("Enter the Github Username : ")
    url = "https://github.com/" + x

    user_file = urllib2.urlopen(url)
    user_html = user_file.read()
    user_file.close()

    soup = BeautifulSoup(user_html, 'html.parser')

    #Find all occurrences of the needed span class
    data = soup.find_all('span', attrs={'class': 'counter'})

    for i in data:
        l.append(i.string)

Get_Details()

#Strip useless text from list elements
l = map(lambda s: s.strip(), l)
d = np.array(l)

print "User Details"
for i in range(0,4):
    print str(type[i]) + " : " + str(d[i])