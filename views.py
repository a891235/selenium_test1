from django.shortcuts import render
from xml.dom.minidom import Document
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import time
import os
a=input("請輸入關鍵字:")
time.sleep(5)  
path="C:/Users/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.dcard.tw/f")
search = driver.find_element_by_name("query")
search.clear()
search.send_keys(a)
search.send_keys(Keys.RETURN)
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sc-d6aee74c-1"))
    )
for i in range(3):    
 js="var q=document.documentElement.scrollTop=20000"  
 driver.execute_script(js)  
 time.sleep(3)  
title = driver.find_elements_by_class_name("sc-b205d8ae-3")
for title in title:
     print(title.text)
     print (title.get_attribute("href"))
     