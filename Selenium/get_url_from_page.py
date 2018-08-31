import re
import linkGrabber
from selenium import webdriver

# Find all the urls/links using linkGrabber

# links = linkGrabber.Links("https://google.com")
# l = links.find(limit=10)
# Fetch all the links using the href property value
# for i in l:
#     print i["href"]

# Find all the links using webdriver and Xpath

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation

ids = driver.find_elements_by_xpath("//*[@href]")   # Fetch the href paths using xpath

for ii in ids:
    print ii.get_attribute("href")

driver.close()  # Close the driver
