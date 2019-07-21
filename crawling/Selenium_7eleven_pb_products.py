from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from random import random

drv = webdriver.Chrome('chromedriver.exe')

url = "http://www.7-eleven.co.kr/product/7prodList.asp"
drv.get(url)

drv.find_element_by_class_name('btn_more').click()

text_main = drv.page_source
bs_text_main = BeautifulSoup(text_main, "html.parser")

main_list = bs_text_main.find("ul", {"id": "listUl"})

main_list_a = main_list.find_all("a", class_ = "btn_product_01")
print(main_list_a[0])
print(main_list_a[0].attrs["href"])

scripts = [main_list_a[n].attrs["href"][12:] for n in range(len(main_list_a))]

print(scripts[0])

df_prod = pd.DataFrame()
for n in range(len(scripts)):
    print(n)
    drv.execute_script(scripts[n])
    time.sleep(random() * 3)
    
    text = drv.page_source
    text_prod = BeautifulSoup(text, "html.parser")
    
    prod_name = text_prod.find("strong", class_ = "tit_product_view").text
    prod_comp = text_prod.find_all("span", class_ = "tit_3depth")[1].text
    prod_price = text_prod.find("span", class_ = "product_price").find("strong").text
    df_prod_sub = pd.DataFrame({"obs": [n], "prod_name": [prod_name], "prod_comp": [prod_comp], "prod_price": [prod_price]})
    
    df_prod = df_prod.append(df_prod_sub)
    
df_prod.head()



