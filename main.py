from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Selenium - библиотека для автоматизации действий веб браузера, скрапинга
# запускаем браузер
s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://aliexpress.ru/')
time.sleep (10)#задержка для ввода капчи
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
tovars = soup.find_all('div', class_='product-snippet_ProductSnippet__name__52z59')
prices = soup.find_all('div', class_='snow-price_SnowPrice__mainM__azqpin')

for tovar, price in zip(tovars, prices):
    print (f"Название товара: {tovar.text} | Цена: {price.text} рублей")


# Это пример парсинга. Вам необходимо спарсить 1 страницу каталога любого сайта на выбор.
#сайты не должны повторяться
# Спарсить необходимо только Заголовки и описание.

