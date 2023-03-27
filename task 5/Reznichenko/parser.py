from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import urllib.request
import requests
import psycopg2


dct = {}
s = Service('C:\chromedriver.exe')
browser = webdriver.Chrome(service=s)
url = 'https://fishki.net/1839329-samye-znamenitye-kartiny-mira-shedevry-mirovoj-zhivopisi.html'
browser.get(url)
html_text = browser.page_source
#page = requests.get(url)
soup = BeautifulSoup(html_text, 'lxml')
count = 1
for i in soup.find_all("div", class_="gallery gallery-image"):
    dct[count] = {}
    str = i.find("h2", itemprop="name").string
    try:
        author = str.split('«')[0].replace(',', '').replace('.', '').strip()
        name = str.split('«')[1].split('»')[0].replace(',', '').replace('.', '').strip()
        date = str.split('»')[1].replace(',', '').replace('.', '').strip()
    except IndexError:
        author = 'Рафаэль Санти'
        name = 'Секстинская мадонна'
        date = '1512'
    dct[count]['author'] = author
    dct[count]['name'] = name
    dct[count]['date'] = date
    description = i.find("div", class_="container_gallery_description").text.replace('\n', '').replace('\t', '')
    dct[count]['description'] = description
    src = i.find("div", class_="picture-relative").find("a").find("img").get("src")
    dct[count]['img_url'] = src
    count += 1


count = 1
for i in dct:
    try:
        req = urllib.request.Request(dct[i]['img_url'], headers={'User-Agent': 'Mozilla/5.0'})
        path = f'img/img{count}.jpeg'
        dct[i]['img_path'] = path
        with open(path, "wb") as f:
            with urllib.request.urlopen(req) as r:
                f.write(r.read())
    except TypeError:
        pass
    count += 1


conn = psycopg2.connect(dbname='db', user='postgres', password='Q1w2e3r4', host='localhost')
cursor = conn.cursor()
cursor.execute('''TRUNCATE public.pictures''')
for i in dct:
    text = f"""INSERT INTO public.pictures(
        id, name, author, year, description, image_url, image_path)
        VALUES ({i}, '{dct[i]['name']}', '{dct[i]['author']}', '{dct[i]['date']}', '{dct[i]['description']}', '{dct[i]['img_url']}', '{dct[i]['img_path']}');"""
    cursor.execute(text)
conn.commit()
conn.close()