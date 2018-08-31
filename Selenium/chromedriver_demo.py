import time
import re
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/39400/Desktop/chromedriver") # Link to the downloaded chrome driver
driver.get("https://google.com/")  # URL for navigation
doc = driver.page_source

#doc = doc.encode("utf-8")
#print(doc)

# Find by ID
# try:
#     x = driver.find_element_by_id("123")
#     print "Successful"
#     print x
# except Exception as e:
#     print e
#     print "ID not found"

# Find by Tag
# try:
#     x = driver.find_element_by_tag_name("img")
#     print "Successful"
# except Exception as e:
#     print e
#     print "Could not find the tag name"
# driver.close()

# Get all the ID element items
# try:
#     ids = driver.find_elements_by_xpath("//*[@id]")  # Get the id using paths
#     for i in ids:
#         print i.get_attribute("id")  # Get the id attribute value of all the list elements
# except Exception as e:
#     print "Exception encountered"
#     print e
# driver.close()

# Get the link by text
# try:
#     driver.find_element_by_link_text("Gmail")
#     print("Passed")
# except Exception as e:
#     print("Failed")
#     print e
# driver.close()

# Get the link by partial text
# try:
#     driver.find_element_by_partial_link_text("Gmail")
#     print("Passed")
# except Exception as e:
#     print("Failed")
#     print e
# time.sleep(2)
# driver.close()

# Get all the class elements
try:
    classes = driver.find_elements_by_xpath("//*[@class]")
    for c in classes:
        print c.get_attribute("class")
except Exception as e:
    print "Failed"
    print e
driver.close()