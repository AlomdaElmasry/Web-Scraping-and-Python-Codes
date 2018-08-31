from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation

time.sleep(2)   # Perform sleep operation
driver.refresh()  # Refresh the webpage
time.sleep(2)
driver.close()  # Close the driver