from selenium import webdriver
import time
import re

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation

time.sleep(4)   # Perform sleep operation
driver.set_window_size(1024,768)    # Set the window size
time.sleep(4)   
driver.maximize_window()    # Maximise the window
time.sleep(4)
driver.close()  # Close the driver