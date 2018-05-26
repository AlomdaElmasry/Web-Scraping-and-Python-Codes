from bs4 import BeautifulSoup
import requests
import urllib2
import urllib

def get_image_links(url):
    image_file = urllib2.urlopen(url)
    image_html = image_file.read()
    image_file.close()

    soup = BeautifulSoup(image_html, "html.parser")

    image_list = []

    for ul in soup.find("ul", attrs={'class' : "filmstrip"}):
        for img in ul.find_all("img"):
            image_list.append(img["src"])

    # print image_list
    for i in image_list:
        full_name = i
        x = full_name.split('rb/')
        print x
        urllib.urlretrieve(full_name, x[1])


url = "https://bingwallpaper.com/"
get_image_links(url)
