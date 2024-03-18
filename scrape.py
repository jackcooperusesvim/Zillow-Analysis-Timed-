from selenium import webdriver
from selenium.webdriver.common.by import By
import time
states = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

# This is just a file with my zip code, which is in gitignore
with open("myzip.txt") as file:
    myzip = file.readlines()


driver = webdriver.Safari()
driver.get("https://www.redfin.com/zipcode/89052")
input("enter once loaded")


elem = driver.find_element(By.XPATH, "//*")
source_code = elem.get_attribute("outerHTML")

with open("index.html","wb") as file:
    file.write(source_code.encode('utf-8'))


# for input in states:
#     search_box = driver.find_element(By.CSS_SELECTOR,'input[placeholder="Add another location"]') 
#     search_box.send_keys(input)
#     next = driver.find_element(By.CSS_SELECTOR,'a[title="Next page"]')
#     reset = driver.find_element(By.CSS_SELECTOR,'button[aria-label="Remove Tag"]')
#     
#
