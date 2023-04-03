from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s = Service('C:\data\hrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://nizagams.ru/20_best_boardgames/')
time.sleep (1)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
games=soup.find_all('h2', class_ = 'vc_custom_heading' )
descriptions=soup.find_all('div', class_="woodmart-title-container woodmart-text-block reset-last-child font-primary wd-font-weight- wd-fontsize-l" )
#Начало ультракостыля, не забыть спросить, как это исправить
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
descriptions.insert(14,'Не указано')
descriptions.insert(15,'Не указано')
descriptions.insert(18,'Не указано')
#Конец ультракостыля, надеюсь меня не пустят на британский флаг за это
gameanddescription = dict(zip(games,descriptions))
for key in gameanddescription:
    print('*', key, gameanddescription[key], sep='\n')