from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
states = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

driver = webdriver.Chrome()
driver.get("https://www.zillow.com/")
time.sleep(1)
search_box = driver.find_element(By.CSS_SELECTOR,'input[placeholder="Enter an address, neighborhood, city, or ZIP code"]') 
search_box.send_keys(states[0])

search_box.send_keys(Keys.ENTER)
time.sleep(5)


search_box = driver.find_element(By.CSS_SELECTOR,'input[placeholder="Add another location"]') 
next = driver.find_element(By.CSS_SELECTOR,'a[title="Next page"]')
reset = driver.find_element(By.CSS_SELECTOR,'button[aria-label="Remove Tag"]')
next.click()
time.sleep(5)
reset.click()
time.sleep(5)
search_box.send_keys(states[1])
search_box.send_keys(Keys.ENTER)
time.sleep(5)





# for input in states:
#     search_box = driver.find_element(By.CSS_SELECTOR,'input[placeholder="Add another location"]') 
#     search_box.send_keys(input)
#     next = driver.find_element(By.CSS_SELECTOR,'a[title="Next page"]')
#     reset = driver.find_element(By.CSS_SELECTOR,'button[aria-label="Remove Tag"]')
#     
#
