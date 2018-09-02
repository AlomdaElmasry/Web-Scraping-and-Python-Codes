from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver", chrome_options=chrome_options) # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation

time.sleep(5)

driver.close()