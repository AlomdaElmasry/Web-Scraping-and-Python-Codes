import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd


def topSongs():

    url = "http://www.billboard.com/charts/hot-100"
    songs_file = urllib2.urlopen(url)
    songs_html = songs_file.read()
    songs_file.close()

    soup = BeautifulSoup(songs_html, 'html.parser')

    # Forming the structure for the song details
    title = soup.find_all('div', attrs={'class' : 'chart-row__title'})

    song = []
    artist = []

    # Getting the name of the song
    for h2 in soup.find_all('h2', attrs={'class' : 'chart-row__song'}):
        song.append(h2.text)

    # Getting the name of the artist
    for span in soup.find_all('span', attrs={'class' : 'chart-row__artist'}):
        artist.append(span.text)

    print song
    print artist


topSongs()