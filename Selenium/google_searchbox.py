import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation


search = driver.find_element_by_id("lst-ib")
search.send_keys("ind vs eng")
search.send_keys(Keys.RETURN)
time.sleep(5)
search.clear()
time.sleep(5)
driver.close()