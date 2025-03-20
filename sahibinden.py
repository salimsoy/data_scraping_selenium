from selenium import webdriver
import undetected_chromedriver as uc
from time import sleep
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


options = uc.ChromeOptions()
driver = uc.Chrome(options=options)

driver.get('https://www.sahibinden.com/')
print("reCAPTCHA varsa elle geç...")
sleep(30)

driver.find_element(By.XPATH, '//*[@id="searchText"]').send_keys("bmw 320i")
driver.find_element(By.XPATH, '//*[@id="searchSuggestionForm"]/button').click()

sleep(6)
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')\
    .click()
    

wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchResultsSearchForm"]/div[1]/div[4]/div[3]/div[2]/ul/li[2]/a')))
element.click()

sleep(5)

item_title=driver.find_elements(By.XPATH,'//*[@id="searchResultsTable"]/tbody/tr/td[3]')
item_price=driver.find_elements(By.XPATH,'//*[@id="searchResultsTable"]/tbody/tr/td[7]')
item_model=driver.find_elements(By.XPATH,'//*[@id="searchResultsTable"]/tbody/tr/td[2]')
item_date=driver.find_elements(By.XPATH,'//*[@id="searchResultsTable"]/tbody/tr/td[4]')
item_km=driver.find_elements(By.XPATH,'//*[@id="searchResultsTable"]/tbody/tr/td[5]')

title_list = []
price_list = []
model_list = []
date_list = []
km_list = []

for title in item_title:
    title_list.append(title.text)

for price in item_price:
    price_list.append(price.text)
    
for model in item_model:
    model_list.append(model.text)
    
for date in item_date:
    date_list.append(date.text)

for km in item_km:
    km_list.append(km.text)
    
print(title_list)
print(price_list)
print(model_list)
print(date_list)
print(km_list)

driver.close()

dfs = pd.DataFrame(zip(title_list,price_list,model_list,date_list,km_list),columns=["title", "price", "model", "date", "km"])




