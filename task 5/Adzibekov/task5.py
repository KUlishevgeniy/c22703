from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import psycopg2

connection = psycopg2.connect(dbname='dbdata',
                                  user='postgres', password='Q1w2e3r4',
                                  host='localhost')
cursor = connection.cursor()

s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.svyaznoy.ru/search?q=%D1%80%D0%B5%D0%B4%D0%BC%D0%B8+%D0%BD%D0%BE%D1%82+11')
time.sleep (10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')

phones = soup.find_all('span', class_="b-product-block__name")
prices = soup.find_all('span', class_="b-product-block__visible-price")
images = soup.find_all('img', class_="lazy-loaded")

for i in range(len(images)):
    images[i] = images[i]['src']

creat_table="""create table svyaznoy
    (id serial primary key, phone varchar(60),
    price varchar(60),
    image varchar(300))"""
cursor.execute(creat_table)


for phone, price, image in zip(phones, prices, images):
    qwery=f"""INSERT INTO public.svyaznoy(
	    phone, price, image)
	    VALUES 
	    ('{phone.text}','{price.text}','{image}')"""
    cursor.execute(qwery)
    connection.commit()

