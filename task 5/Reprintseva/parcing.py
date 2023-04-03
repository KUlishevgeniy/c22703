from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.avito.ru/all/avtomobili/chevrolet-ASgBAgICAUTgtg32lyg?cd=1')
time.sleep (10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
mashinas=soup.find_all('div', class_='iva-item-titleStep-pdebR')
prices=soup.find_all('span', class_='price-root-RA1pj price-listRedesign-GXB2V')
#https://40.img.avito.st/image/1/1.p8Bvdba1Cyl51bEpLRPv1VjXCSnR3qkoYdQJKw.XzMqhOcm4UWnTGMWcX4rJjriSxk1fixY4DLLT2MPkzk
opisanies=soup.find_all('div', class_='iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL')
#for mashina, price, opisanie in zip(mashinas, prices,opisanies):
    #print(f"Название машины: {mashina.text} | Цена: {price.text} рублей | Описание: {opisanie.text}" )
import psycopg2
connection = psycopg2.connect(dbname='dbdata',
                                  user='postgres', password='Q1w2e3r4',
                                  host='localhost')
cursor = connection.cursor()
creat_table="""CREATE TABLE avito666
    (id serial primary key, "Автомобиль" varchar(100),
    "Цена" varchar(100),
    "Описание" varchar(50000))"""
cursor.execute(creat_table)
connection.commit()
for mashina, price, opisanie in zip(mashinas, prices, opisanies):
            query = """ INSERT INTO public.avito666(
            "Автомобиль", "Цена", "Описание")
            VALUES (%s,%s,%s);"""
            record_to_insert = (mashina.text, price.text, opisanie.text)
            cursor.execute(query, record_to_insert)
connection.commit()
cursor.close()
connection.close()