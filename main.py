from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import psycopg2
import wget
import time

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()



s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.eapteka.ru/goods/vitaminy_i_bad/')
time.sleep (10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')

creat_table="""create table cases
    (id serial primary key, name varchar(150),
    price varchar(150),
    scr varchar(150))"""
cursor.execute(creat_table)
connection.commit()


names= soup.find_all('h5', class_="listing-card__title")
prices = soup.find_all('span', class_="listing-card__price-new")
pictures = soup.find_all('a', class_="listing-card__link")
for i in range(len(names)):
    url = pictures[i].find('img')['src']
    filename = f"C:\\Users\\Админ\\картинки\\{i}.jpg"
    wget.download(url, filename)

    insert_qwery = """INSERT INTO public.cases(name, price, scr)
    VALUES( %s, %s, %s);"""
    record_to_insert = (names[i].text, prices[i].text, filename)
    cursor.execute(insert_qwery, record_to_insert)
    connection.commit()

cursor.close()
connection.close()
