from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.svyaznoy.ru/search?q=%D1%80%D0%B5%D0%B4%D0%BC%D0%B8+%D0%BD%D0%BE%D1%82+11')
time.sleep (10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
phones = soup.find_all('span', class_="b-product-block__name")
prices = soup.find_all('span', class_="b-product-block__visible-price")
#for phone, price in zip(phones, prices):
    #print(f"Название модели: {phone.text} | Цена: {price.text}" )
import psycopg2
connection = psycopg2.connect(dbname='dbdata',
                                  user='postgres', password='Q1w2e3r4',
                                  host='localhost')
cursor = connection.cursor()
for phone, price in zip(phones, prices):
            query = """ INSERT INTO public.svyaznoy(
            "phone", "price")
            VALUES (%s,%s);"""
            record_to_insert = (phone.text, price.text)
            cursor.execute(query, record_to_insert)
connection.commit()
cursor.close()
connection.close()

