import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.993dy.com/vod-detail-id-10549.html')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
print(r.text)
aTagObj = soup.find_all('a', class_="adds")
print(aTagObj)
# print(r.text)