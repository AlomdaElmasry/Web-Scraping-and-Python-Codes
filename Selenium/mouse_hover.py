import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation

element = driver.find_element_by_link_text("Gmail")
hover = webdriver.ActionChains(driver).move_to_element(element) # Create an action chain with the move to operation
hover.perform()
driver.close()