from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import wget
import time

s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://amital.ru/Hudozhyestvyennaya-lityeratura-c1.html?sort=p.sort_order&order=ASC&page=1')
time.sleep (10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')

products=soup.find_all('div', class_='product-name')
prices=soup.find_all('div', class_='final-price')
pictures=soup.find_all('div', class_="product-img")

import psycopg2
connection = psycopg2.connect(dbname='dbdata',
                              user='postgres', password='zhemchug2021',
                                               host='localhost')
cursor=connection.cursor()

creat_table="""CREATE TABLE books
    ("Название книги" varchar(100),
    "Цена" varchar(100),
    "Картинка" varchar(100))"""
cursor.execute(creat_table)
connection.commit()

for i in range (5):
    print(i)
    url =pictures[i].find('img')['src']
    filename = f"C:\\Users\\mary_\\Downloads\\photos\\{i}.jpg"
    wget.download(url, filename)

    query=""" INSERT INTO public.books(
        "Название книги", "Цена", "Картинка")
        VALUES (%s,%s,%s);"""
    record_to_insert = (products[i].text, prices[i].text, filename)
    cursor.execute(query, record_to_insert)
connection.commit()
cursor.close()
connection.close()