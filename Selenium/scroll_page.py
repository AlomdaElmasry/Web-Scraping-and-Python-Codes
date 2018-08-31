from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://github.com/")  # URL for navigation

elem = driver.find_element_by_tag_name("html")  # Find the html tag
elem.send_keys(Keys.END)    # Go to the end of the tag
time.sleep(3)   # Perform sleep operation
elem.send_keys(Keys.HOME)   # Go to the top/home of the tag
time.sleep(3)   # Perform sleep operation
driver.close()  # Close the driver
