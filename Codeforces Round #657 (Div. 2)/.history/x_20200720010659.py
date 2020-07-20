import requests
from bs4 import BeautifulSoup
import lxml.html
r = requests.get('https://www.993dy.com/vod-detail-id-10549.html')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
# prin/html/body/div[4]/div[3]/div[3]

l = list(soup.findAll('div'))
print(l)

# print(r.text)