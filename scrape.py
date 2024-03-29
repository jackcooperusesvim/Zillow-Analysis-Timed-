from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import time
states = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

# This is just a file with my zip code, which is in gitignore
with open("myzip.txt") as file:
    myzip = file.readlines()


driver = webdriver.Safari()
driver.get("https://www.redfin.com/zipcode/89052")
time.sleep(2)

print("Checking for code")
elem = driver.find_element(By.XPATH, "//*")
source_code = elem.get_attribute("outerHTML")

if source_code == None:
    raise Exception("The code is a lie")

print("Parsing HTML")
parsed_html = BeautifulSoup(source_code.encode("utf-8"),"lxml")

print("Writing HTML")
with open("index.html","w") as file:
    file.write(parsed_html.prettify())

print("looking for HomeCardsContainer flex flex-wrap")

#Remove the Ads
def get_html(driver):
    elem = driver.find_element(By.XPATH, "//*")
    return BeautifulSoup(elem.get_attribute("outerHTML"),"lxml")

HCsC = []
pagenum=1
home_total=1
while True:
    i=1
    next_button = driver.find_element(By.CSS_SELECTOR, "button[class~=bp-Button][aria-label~=next]")
    parsed_html = get_html(driver)
    while True:
        parsed_div = parsed_html.select_one("div[id~=MapHomeCard_{}]".format(i))
        if parsed_div == None:
            break
        HCsC.append(parsed_div)
        i+=1
        home_total+=1
    print("done with page {} \nNow we click next".format(pagenum))
    ActionChains(driver).move_to_element(next_button).perform()
    input("hit enter to go to the next page")
    if next_button == None:
        break
    next_button.click()
    pagenum+=1
    
# print(HCsC)
print("Found {} Homes after searching {} pages".format(home_total,pagenum))
input()

# for input in states:
#     search_box = driver.find_element(By.CSS_SELECTOR,'input[placeholder="Add another location"]') 
#     search_box.send_keys(input)
#     next = driver.find_element(By.CSS_SELECTOR,'a[title="Next page"]')
#     reset = driver.find_element(By.CSS_SELECTOR,'button[aria-label="Remove Tag"]')
#     
#
