
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.mvideo.ru/product-list-page?q=%D0%B8%D0%B3%D1%80%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B8&category=noutbuki-118')
time.sleep(10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')

laptops = soup.find_all('div', class_='product-title_text')
prices = soup.find_all('span', class_='price_main-value')

for laptop, price in zip(laptops,prices):
    print(f'Модель ноутбука: {laptop.text} | Цена: {price.text} рублей')