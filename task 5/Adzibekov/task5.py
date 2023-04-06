from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import psycopg2
import wget

s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.svyaznoy.ru/search?q=%D1%80%D0%B5%D0%B4%D0%BC%D0%B8+%D0%BD%D0%BE%D1%82+11')
time.sleep (10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')

phones = soup.find_all('span', class_="b-product-block__name")
prices = soup.find_all('span', class_="b-product-block__visible-price")
image = soup.find_all('img', class_="lazy-loaded")
str_image=[]
for i in range(len(image)):
    str_image.append(image[i])
str_image=str(str_image)
str_image=re.findall(r'src="(.*?)"', str_image)
for i in range(len(str_image)):
    str_image[i]='https:'+str_image[i]
connection = psycopg2.connect(dbname='dbdata',
                                  user='postgres', password='Q1w2e3r4',
                                  host='localhost')
cursor = connection.cursor()

creat_table="""create table svyaznoy
    (id serial primary key, phone varchar(60),
    price varchar(60),
    image varchar(300))"""
cursor.execute(creat_table)

for phone, price, image in zip(phones, prices, images):
    qwery=f"""INSERT INTO public.svyaznoy(
	    phone, price, image)
	    VALUES 
	    ('{phone.text}','{price.text}','{image.text}')"""
    cursor.execute(qwery)
    connection.commit()

    for i in range(1, len(str_image) + 1):
        puti = r'C:\Users\kingo\PycharmProjects\pythonProject2\TOP' + str(i) + '.jpeg'
        qwery = f"""UPDATE public.svyaznoy
            SET image='{puti}'
            WHERE id={i}"""
        cursor.execute(qwery)
        connection.commit()


