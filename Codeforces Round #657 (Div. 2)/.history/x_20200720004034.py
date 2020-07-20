import requests
import bs4
r = requests.get('https://www.993dy.com/vod-detail-id-10549.html')
r.encoding = 'utf-8'
aTagObj = soup.find_all('a', class_="adds")
print(aTagObj)
# print(r.text)