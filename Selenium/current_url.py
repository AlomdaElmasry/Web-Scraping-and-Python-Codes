from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation

print("Current url before click : " + str(driver.current_url))  # Get the current url of the webpage

elem = driver.find_element_by_link_text("About")    # Find the link element using the text
time.sleep(2)   # Perform sleep operation
elem.click()    # Click on the link
print("Current url after performing the click operation : " + str(driver.current_url))
time.sleep(2)
driver.back()   # Go back (Webpage)
driver.close()  # Close the driver
