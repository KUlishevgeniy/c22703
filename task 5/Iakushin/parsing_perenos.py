from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import wget
import psycopg2
import re
s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://music.yandex.ru/chart')
time.sleep (1)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
nazvanie_treka=soup.find_all('a', class_='d-track__title deco-link deco-link_stronger')
dlitelnost=soup.find_all('div', class_='d-track__info d-track__nohover')
avtor=soup.find_all('span', class_='d-track__artists')
cartinki=soup.find_all('img', class_='entity-cover__image deco-pane')
str_cartinki=[]
for i in range(len(cartinki)):
    str_cartinki.append(cartinki[i])
str_cartinki=str(str_cartinki)
str_cartinki=re.findall(r'src="(.*?)"',str_cartinki)
for i in range(len(str_cartinki)):
    str_cartinki[i]='https:'+str_cartinki[i]
#for i in range(len(str_cartinki)):
    #wget.download(str_cartinki[i], 'TOP'+str((i+1))+'.jpeg')

connection = psycopg2.connect(dbname = 'testDB',
                           user='postgres', password='Q1w2e3r4',
                           host='localhost')
cursor=connection.cursor()
for nazvanie_treka, dlitelnost, avtor in zip(nazvanie_treka, dlitelnost, avtor):
    qwery=f"""INSERT INTO public.chart(
	    nazvanie_treka, avtor, dlitelnost)
	    VALUES 
	    ('{nazvanie_treka.text}','{avtor.text}','{dlitelnost.text}')"""
    cursor.execute(qwery)
    connection.commit()
for i in range(1,len(str_cartinki)+1):
    puti = r'C:\Users\kingo\PycharmProjects\pythonProject2\TOP' + str(i) + '.jpeg'
    qwery=f"""UPDATE public.chart
        SET photo='{puti}'
        WHERE id={i}"""
    cursor.execute(qwery)
    connection.commit()
