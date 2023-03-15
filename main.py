from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://aliexpress.ru/')
time.sleep (10)#задержка для ввода капчи
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('div', class_='product-snippet_ProductSnippet__name__52z59')
prices = soup.find_all('div', class_='snow-price_SnowPrice__mainM__azqpin')

for product, price in zip(products, prices):
    print (f"Название товара: {product.text} | Цена: {price.text} рублей")



