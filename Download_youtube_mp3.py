#!/usr/bin/python2.7

from bs4 import BeautifulSoup
import urllib2
from prettytable import PrettyTable
import sys
import os
from urlparse import urlparse
import requests
import urllib

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*db / %db" % (percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize:  # near the end
            print "\nDownload complete"
            sys.stderr.write("\n")
    else:  # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))


x = raw_input("Enter your query : ")

query = x.lower()
quoted_query = urllib2.quote(query)

url = "https://www.youtube.com/results?search_query=" + quoted_query

# add header
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

request = urllib2.Request(url, headers=headers)
data_file = urllib2.urlopen(request)
data_html = data_file.read()
data_file.close()

soup = BeautifulSoup(data_html, 'html.parser')

title = []
ref = []

for h3 in soup.find_all("h3", attrs={"class":"yt-lockup-title"}):
    title.append(h3.find('a').contents[0])
    ref.append(h3.find('a')['href'])

sequence = ["S.No", "Title"]

t = PrettyTable(sequence)

for i in range(0, len(title)):
    t.add_row([i+1, title[i]])

if len(title) != 0:
    print color.BOLD + color.CYAN + "\nResults : " + color.END

    print t

    choice = raw_input(color.CYAN + color.BOLD + "\nEnter your choice (numerical) : " + color.END)

    if int(choice) >= 1 and int(choice) <= len(title):
        video_url = "https://www.youtube.com" + str(ref[int(choice) - 1])

        temp_download_url = "http://www.youtubeinmp3.com/download/?video=" + str(video_url)

        r = requests.post(temp_download_url)

        soup = BeautifulSoup(r.text, "html.parser")

        for a in soup.find_all("a", attrs={"id": "download"}):
            final_download_url = "http://www.youtubeinmp3.com" + str(a['href'])

        print final_download_url

        path = "file.mp3"

        urllib.urlretrieve(final_download_url, path, reporthook)

    else:
        print "Invalid entry."
        quit()

else:
    print color.BOLD + color.CYAN + "Sorry, no results found." + color.END
    quit()