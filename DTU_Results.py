from bs4 import BeautifulSoup
import urllib2
import requests


def get_Results():
    url = "http://www.exam.dtu.ac.in/result.htm"
    result_file = urllib2.urlopen(url)
    result_html = result_file.read()
    result_file.close()

    soup = BeautifulSoup(result_html, "html.parser")

    li = []

    for a in soup.find_all("a"):
        li.append(a.text)

    li = map(lambda s: s.strip(), li)

    final_li = []

    for i in range(12, len(li)):
        final_li.append(li[i])

    del final_li[len(final_li) - 1]

    print "\n"

    for i in final_li:
        print "-->  " + str(i)


if __name__ == "__main__":
    get_Results()