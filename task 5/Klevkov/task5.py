
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import time
import psycopg2



connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()

s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://lcls.ru/collection/odezhda')
time.sleep(10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')

brands = soup.find_all('div', class_="product-preview__brand")
titles = soup.find_all('div', class_="h2 product-preview__title")
prices = soup.find_all('span', class_="product-preview__price-cur")
images = soup.find_all('img', class_='lazyload product-preview__img-1 entered loaded')

for i in range(len(images)):
    images[i] = images[i]['src']

creat_table="""create table clothes
    (id serial primary key, brand varchar(60),
    title varchar(60),
    price varchar(60),
    image varchar(300))"""
cursor.execute(creat_table)


for brand, title, price, image in zip(brands, titles, prices, images):
    qwery=f"""INSERT INTO public.clothes(
	    brand, title, price, image)
	    VALUES 
	    ('{brand.text}','{title.text}','{price.text}','{image}')"""
    cursor.execute(qwery)
    connection.commit()