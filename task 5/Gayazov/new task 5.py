from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import psycopg2
s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://nizagams.ru/20_best_boardgames/')
time.sleep(1)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
games = soup.find_all('h2', class_ = 'vc_custom_heading' )
descriptions = soup.find_all('div', class_="woodmart-title-container woodmart-text-block reset-last-child font-primary wd-font-weight- wd-fontsize-l" )
for i in range(len(descriptions)):
    descriptions[i] = descriptions[i].text
for i in range(len(descriptions)):
    descriptions[i] = descriptions[i].replace('\n', '')
    descriptions[i] = descriptions[i].replace('\t', '')
for i in range(len(games)):
    games[i] = games[i].text
del descriptions[0:3]
del descriptions[2]
del descriptions[10:12]
del descriptions[13:15]
descriptions.insert(14, 'Не указано')
descriptions.insert(15, 'Не указано')
descriptions.insert(18, 'Не указано')
pictures = soup.find_all('img', class_='attachment-woocommerce_thumbnail size-woocommerce_thumbnail')
for i in range(len(pictures)):
    pictures[i] = pictures[i]['src']
del pictures[2:9]
del pictures[3]
del pictures[4]
del pictures[5]
del pictures[6:10]
del pictures[8]
del pictures[9]
del pictures[10]
del pictures[11]
del pictures[12]
del pictures[13]
del pictures[14:16]
del pictures[15]
del pictures[17]
del pictures[18]
del pictures[19]
del pictures[20]
del pictures[21]
connection = psycopg2.connect(dbname='Testbase', user='postgres', password='Q1w2e3r4', host='Localhost')
cursor = connection.cursor()
for i in range(20):
    a = (games[i], descriptions[i], pictures[i])
    cursor.execute("INSERT into testtable (game,description,picture) VALUES (%s, %s, %s)", a)
    connection.commit()
cursor.close()