from typing import Text
from selenium import webdriver
import undetected_chromedriver
import requests
import time

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--disable-notifications")
options.add_argument("disable-infobars")
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--lang=en-US")
undetected_chromedriver.install()
driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


driver.get('https://swapi.dev/')


print("\n TEST 1: Verifcation Check\n")
request=driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
time.sleep(1)
verify_check=driver.find_element_by_xpath('//pre[@id="interactive_output"]').text
if "404" in verify_check:
    print("404 ERROR")
else:
    print("\n[++] Succesful Response\n")

time.sleep(1)

print("\n TEST 2: Height >200\n")

name=[]
count=0
page=1
for i in range(9):
    url = "https://swapi.dev/api/people/"

    querystring = {"page":str(page)}

    response = requests.request("GET", url, params=querystring)

    data=(response.json()["results"])

    

    for user in data:
        count+=1

        height=user['height']

        if int(height)>=200:
            name.append(user['name'])



print("\n TEST 3: 10 user matches\n")

names="Darth Vader. Chewbacca, Roos Tarpals, Rugor Nass, Yarael Poof, Lama Su, Tuan Wu, Grievous, Tarfful, Tion Medon"
chk=0
for person in name:
    if person in names:
        chk+=1

if chk==10:
    print(" All Same Users")
else:
    print("different users")


print("\n TEST 3: 82 count\n")

if count==82:
    print("total 82 users")
else:
    print("more users")
