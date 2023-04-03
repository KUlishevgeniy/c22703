om bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import wget
import time

s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.chitai-gorod.ru/catalog/kanctovars/tovary-dlya-hudozhnikov-3441')
time.sleep (10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')

products=soup.find_all('div', class_='product-title__head')
prices=soup.find_all('div', class_='product-price')
pictures=soup.find_all('picture', class_="product-picture")

import psycopg2
connection = psycopg2.connect(dbname='dbdata',
                              user='postgres', password='zhemchug2021',
                                               host='localhost')
cursor=connection.cursor()

creat_table="""CREATE TABLE artist666
    ("Название товара" varchar(1000),
    "Цена" varchar(100),
    "Картинка" varchar(100))"""
cursor.execute(creat_table)
connection.commit()

for i in range (10):
    print(i)
    url =pictures[i].find('img')['src']
    filename =f"/Users/katya/Desktop/pars/photos/{i}.jpg"
    wget.download(url, filename)

    query=""" INSERT INTO public.artist666(
        "Название товара", "Цена", "Картинка")
        VALUES (%s,%s,%s);"""
    record_to_insert = (products[i].text, prices[i].text, filename)
    cursor.execute(query, record_to_insert)
connection.commit()
cursor.close()
connection.close()