from bs4 import BeautifulSoup
import json
import requests
import re


ans = {}
url = 'https://fishki.net/1839329-samye-znamenitye-kartiny-mira-shedevry-mirovoj-zhivopisi.html'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
count = 1
for i in soup.find_all("div", class_="gallery gallery-image"):
    ans[count] = {}
    a = i.find("h2", itemprop="name").string
    ans[count]['author'] = re.findall(r'([а-яА-ЯёЁ ]+(\[.»])*)', a)[0][0][:-1]
    ans[count]['name'] = re.findall('\«[а-яА-ЯёЁ. ,]+\»', a)
    if ans[count]['name'] == []:
      ans[count]['name'] = '«' + a[a.find('.') + 3:a.find(',')] + '»'
    else:
      ans[count]['name'] = ans[count]['name'][0]

    ans[count]['date'] = re.findall('\d\d\d\d[-–]+\d\d\d\d', a)
    if ans[count]['date'] == []:
        ans[count]['date'] = re.findall('\d\d\d\d\.', a)[0][:-1]
    else:
        ans[count]['date'] = ans[count]['date'][0]
    ans[count]['text'] = str(i.find("div", itemprop="description"))[:-21].replace('\n', '').replace('\t', '')
    ind = ans[count]['text'].find('<!--<p>-->')
    ans[count]['text'] = ans[count]['text'][ind + 10:]
    ans[count]['image_href'] = i.find("div", class_="picture-relative").find("a").get("href")
    count += 1
