from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation

element = driver.find_element_by_link_text("Gmail")
action = webdriver.ActionChains(driver) # Create an action chain
action.context_click(element).perform() # Perform the right click
time.sleep(5)
driver.close()