from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# Selenium - библиотека для автоматизации действий веб браузера, скрапинга
# запускаем браузер
s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.lamoda.ru/c/557/accs-zhenskieaksessuary/?sitelink=topmenuW&l=5')
time.sleep (10)#задержка для ввода капчи
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')

women_products=soup.find_all('div', class_='x-product-card-description__brand-name _brandName_k0rqx_6')
prices=soup.find_all('span', class_='x-product-card-description__price-single x-product-card-description__price-WEB8507_price_no_bold _price_k0rqx_8')
for women_product, price in zip(women_products, prices):
    print(f"Название модели аксессуара: {women_product.text} | Цена: {price.text} рублей")