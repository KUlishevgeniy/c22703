from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# Selenium - библиотека для автоматизации действий веб браузера, скрапинга
# запускаем браузер
s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://music.yandex.ru/chart')
time.sleep (1)#задержка для ввода капчи
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')

nazvanie_treka=soup.find_all('a', class_='d-track__title deco-link deco-link_stronger')
dlitelnost=soup.find_all('div', class_='d-track__info d-track__nohover')
avtor=soup.find_all('span', class_='d-track__artists')
for nazvanie_treka, dlitelnost, avtor in zip(nazvanie_treka, dlitelnost, avtor):
    print(f"Название трека: {nazvanie_treka.text} | Автор {avtor.text} | Длительность: {dlitelnost.text}")