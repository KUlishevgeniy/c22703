from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Selenium - библиотека для автоматизации действий веб браузера, скрапинга
# запускаем браузер
s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.avito.ru/all/avtomobili/chevrolet-ASgBAgICAUTgtg32lyg?cd=1')
time.sleep (10)#задержка для ввода капчи
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
mashinas=soup.find_all('div', class_='iva-item-titleStep-pdebR')
prices=soup.find_all('span', class_='price-root-RA1pj price-listRedesign-GXB2V')
#https://40.img.avito.st/image/1/1.p8Bvdba1Cyl51bEpLRPv1VjXCSnR3qkoYdQJKw.XzMqhOcm4UWnTGMWcX4rJjriSxk1fixY4DLLT2MPkzk
opisanies=soup.find_all('div', class_='iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL')
for mashina, price, opisanie in zip(mashinas, prices,opisanies):
    print(f"Название машины: {mashina.text} | Цена: {price.text} рублей | Описание: {opisanie.text}" )