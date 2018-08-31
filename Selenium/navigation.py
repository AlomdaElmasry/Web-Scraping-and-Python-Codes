from selenium import webdriver
import time
import re

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation

elem = driver.find_element_by_link_text("About")    # Fetch the link
time.sleep(2)   # Perform Sleep operation
elem.click()    # Perform the click operation
time.sleep(2)
driver.back()   # Revert back to the previous page
time.sleep(2)
driver.forward()    # Move forward
driver.close()  # Close the driver
