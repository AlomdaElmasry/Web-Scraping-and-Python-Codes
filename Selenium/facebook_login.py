import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://facebook.com/")  # URL for navigation

username = raw_input("Enter your username : ")
password = raw_input("Enter your password : ")

time.sleep(5)
element_id = driver.find_element_by_id("email")
element_id.send_keys(username)
element_pass = driver.find_element_by_id("pass")
element_pass.send_keys(password)
element_btn = driver.find_element_by_id("loginbutton")
element_btn.click()
