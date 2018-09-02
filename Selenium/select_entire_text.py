import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation

element = driver.find_element_by_css_selector("body")
element.send_keys(Keys.CONTROL + "a")
time.sleep(5)
driver.close()