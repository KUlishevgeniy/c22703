# pip install selenium bs4


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# from time import sleep


s = Service("C:\\10\\chromedriver.exe")
brow = webdriver.Chrome(service=s)

# brow.get("https://www.kinopoisk.ru/lists/movies/top250/")
brow.get("https://www.revshells.com/")
# sleep(10)

html = brow.page_source

soup = BeautifulSoup(html, "lxml")

# films = soup.find_all(attrs={"class": "styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj"})
buttons = soup.find_all(attrs={"class": "list-group-item list-group-item-action"})

for button in buttons:
    print(button.text)