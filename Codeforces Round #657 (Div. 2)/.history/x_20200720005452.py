import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.993dy.com/vod-detail-id-10549.html')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.content, 'html.parser')
# prin/html/body/div[4]/div[3]/div[3]
x = list(soup.findAll('div'))[4]
x = list(x.findall('div'))[3]
print(x)
# print(r.text)