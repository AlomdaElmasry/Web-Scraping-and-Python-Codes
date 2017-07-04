from bs4 import BeautifulSoup
import requests
import urllib
import urllib2


def get_PDF():
    url = raw_input("Provide the link of the page : ")
    page_file = urllib2.urlopen(url)
    page_html = page_file.read()
    page_file.close()

    soup1 = BeautifulSoup(page_html, "html.parser")


    for button1 in soup1.find_all("button", attrs={"class":"btn btn-default btn-sm btn-buy-tutorial"}):
        for a1 in button1.find_all("a"):
            pdf_page_link = "http://www.tutorialspoint.com" + str(a1['href'])

    print pdf_page_link

    pdf_file = urllib2.urlopen(pdf_page_link)
    pdf_html = pdf_file.read()
    pdf_file.close()

    soup2 = BeautifulSoup(pdf_html, "html.parser")

    for div in soup2.find_all("div", attrs={'class' : "pdf-btn"}):
        for a2 in div.find_all("a"):
            pdf_title = str(a2["title"]) + str(".pdf")

    for a3 in soup2.find_all("a", attrs={"class" : "left"}):
        pdf_link = "http://www.tutorialspoint.com" + str(a3['href'])
            

    print pdf_link
    urllib.urlretrieve(pdf_link, pdf_title)

    #urllib.urlretrieve(pdf_link, final_title)

get_PDF()