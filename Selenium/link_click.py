import time
import re
from selenium import webdriver


driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation

elem = driver.find_element_by_link_text("About")   # Get the link text
driver.implicitly_wait(5)   # Wait operation
elem.click()   # Perform the click operation
time.sleep(5)   # Perform time sleep
driver.close()  # Close the driver