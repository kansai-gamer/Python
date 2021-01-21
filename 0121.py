import requests
import re
from bs4 import BeautifulSoup

url = 'https://gigazine.net/news/20130706-15-cats-in-container/'

html_data = requests.get(url)

soup = BeautifulSoup(html_data.text, 'lxml')


images = []

for img in soup.find_all('img',class_="lazyload"):
    print(img.get("data-src"))
    images.append(img.get("data-src"))

i = 1
for tareget in images:
    re = requests.get(tareget)
    print(re)
    with open('img/' + str(i) + ".jpg", 'wb') as f:
        f.write(re.content)
    i+= 1