import urllib2
from bs4 import BeautifulSoup
import os

def download_repo(url):
    repo_file = urllib2.urlopen(url)
    repo_html = repo_file.read()
    repo_file.close()

    soup = BeautifulSoup(repo_html, "html.parser")

    #print soup

    l = []

    for div in soup.find_all("div", attrs={"class":"d-inline-block mb-1"}):
        for a in div.find_all("a"):
            l.append(a.text)

    l = map(lambda s: s.strip(), l)
    # print l

    url_trim = url.split("?")

    final_l = []

    for i in l:
        final_l.append(str(url_trim[0]) + str("/") + str(i))


    # print final_l

    for i in final_l:
        os.system("git clone " + str(i))
        

download_repo("https://github.com/dushyantRathore?tab=repositories")

