from mechanize import Browser
from bs4 import BeautifulSoup
import requests
import random,string


def generate_random_text(length):
    letter = string.ascii_lowercase
    text = ""
    i = 0
    while i < length:
        letter = random.choice(string.ascii_lowercase)
        text = text + str(letter)
        i+=1

    return text


def mess_up(url):

    browser = Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent',
                      'Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11')]

    response = browser.open(url)

    # print response.read()

    browser.form = list(browser.forms())[0]

    for control in browser.form.controls:
        control.readonly = False
        control.disabled = False

    for control in browser.form.controls:
        if control.type == "text":
            x = generate_random_text(20)
            control.value = x
        elif control.type == "textarea":
            x = generate_random_text(200)
            control.value = x

    browser.submit()


url = raw_input("Enter the url : ")
no = int(raw_input("Enter the number of times you want to spam the form : "))

for i in range(0,no):
    mess_up(url)
