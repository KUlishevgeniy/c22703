from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# Selenium - библиотека для автоматизации действий веб браузера, скрапинга
# запускаем браузер
s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/chehly/chekxly-dlya-telefonov-samsung')
time.sleep (10)#задержка для ввода капчи
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')

# парсим чехольчики на телефончики
brand_n = soup.find_all('span', class_='brand-name')
goods_n = soup.find_all('span', class_='goods-name')
real_prices = soup.find_all('ins', class_='price__lower-price')

for product, real_price, brand in zip(goods_n, real_prices, brand_n):
    print(f"Название чехольчика: {product.text[3:]} | Цена: {real_price.text.strip()} рублей | Продавец: {brand.text}")