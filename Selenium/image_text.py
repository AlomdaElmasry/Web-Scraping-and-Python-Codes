from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation

for element in driver.find_elements_by_tag_name("img"):
    print(element.text)
    print(element.location)
    print(element.size)
    print(element.tag_name)

driver.close()