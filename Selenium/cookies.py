from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation

print(driver.get_cookies())

driver.close()
