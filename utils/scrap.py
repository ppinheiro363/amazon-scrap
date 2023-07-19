from selenium import webdriver
import pandas as pd
from datetime import datetime

from utils.amazon import AmazonScrap
from utils.tasks import Sheet

def create_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.headless = False
     
    return webdriver.Chrome(options=options)

driver = create_driver()

start = AmazonScrap(driver)
sheet = pd.read_excel('Links.xlsx')
new_prices = []

for item in sheet['URL']:

    start.product_page(item)
    try:
        preco = [start.product_whole_price_objt().text, start.product_fraction_price().text]
        preco2 = ','.join(preco)   
        new_prices.append(preco2)  

    except:
        new_prices.append('Valor Não encontrado')
        continue

timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

timestamped_prices = pd.DataFrame(columns=[timestamp])
timestamped_prices[timestamp] = new_prices

sheet = pd.concat([sheet, timestamped_prices], axis=1)

sheet.to_excel('Links.xlsx', index=False)




