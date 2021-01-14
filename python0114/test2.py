import requests
import re
from bs4 import BeautifulSoup

url = 'https://gigazine.net/news/20130706-15-cats-in-container/'

html_data = requests.get(url)

soup = BeautifulSoup(html_data.text, 'lxml')


images = []

for img in soup.find_all('img'):
    print(img.get("data-src"))
    images.append(img.get("data-src"))

print(images)