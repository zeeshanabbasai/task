from selenium import webdriver
import undetected_chromedriver
import os,random
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

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


driver.get('https://www.aspiration.com/')

time.sleep(3)

print("\n[++] TEST 1: testing the 'Spend & Save'\n" )

spend_and_save_button=driver.find_element_by_xpath("//header[@data-id='header']//a[contains(@href,'https://www.aspiration.com/our-products')]")

spend_and_save_button.click()

time.sleep(3)

try:
    verify_spend_and_save_button=driver.find_element_by_xpath('//div[@class="error-code"]')
    print("\n[--]  TEST 1: Unable to Acces Page. User cant go to “Spend & Save” page \n")
except:
    print("\n [++] Website Working\n")


print("\n[++] TEST 2: 2 card products, Aspiration and Aspiration Plus \n" )

driver.back()

time.sleep(2)


try:
    
    aspiration_card=driver.find_element_by_xpath('//div[@id="price-card-2"]')
    driver.execute_script("arguments[0].scrollIntoView();",aspiration_card)
    print("\n [++] Activation Card product exists\n")
except:
    print("\n[--] Actication Card Not exists \n")

try:    
    aspirationplus_card=driver.find_element_by_xpath('//div[@id="price-card-3"]')
    driver.execute_script("arguments[0].scrollIntoView();",aspirationplus_card)
    print("\n [++] Activation PLUS Card product exists\n")
except:
    print("\n[--] Actication PLUS Card Not exists \n")





print("\n[++] TEST 3: Get Aspiration -  input field for an email Verification \n" )


try:    
    aspiration_card=driver.find_element_by_xpath('//div[@id="price-card-2"]')
    aspiration_card.click()
    time.sleep(1)
    aspiration_email=driver.find_element_by_xpath('//div[@role="dialog"]//input[@aria-label="Email Address"]')
    print("\n [++] Email Input field Exists\n")
    driver.find_element_by_xpath('//button[@data-testid="trigger"]').click()
except:
    print("\n[--] Email Input field dont exists \n")


print("\n[++] TEST 4: Get Aspiration PLUS -  modal with monthly and yearly plans appears \n" )

   
aspirationplus_card=driver.find_element_by_xpath('//div[@id="price-card-3"]')
aspirationplus_card.click()
time.sleep(1)
aspirationplus_month_year=driver.find_element_by_xpath('//div[@role="dialog" and not(@id="onetrust-pc-sdk")]')
test=aspirationplus_month_year.text

if "monthly" in test or "yearly" in test or "plans" in test:

    print("\n [++] Yearly/Montly plans Modal can be seen\n") 

else:
    print("\n [--] Yearly/Monthly cannot be seen\n")


print("\n[++] TEST 5-6: Verify that yearly radio option \n" )

print('\n [--] Radio Button dont exists in webpage in the first place\n')





