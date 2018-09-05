import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email = raw_input("Enter your email : ")
password = raw_input("Enter your password : ")

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://accounts.google.com/ServiceLogin/identifier?flowName=GlifWebSignIn&flowEntry=AddSession")  # URL for navigation

element = driver.find_element_by_xpath("//input[@type='email']")
element.send_keys(email + Keys.ENTER)
time.sleep(3)
element = driver.find_element_by_xpath("//input[@type='password']")
element.send_keys(password + Keys.ENTER)
time.sleep(3)
driver.close()