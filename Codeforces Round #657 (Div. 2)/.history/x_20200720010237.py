import requests
from bs4 import BeautifulSoup
import lxml.html
r = requests.get('https://www.993dy.com/vod-detail-id-10549.html')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.content, 'html.parser')
# prin/html/body/div[4]/div[3]/div[3]



html = lxml.html.fromstring(r.content)

html_data = html.xpath("/html/body/div[4]/div[3]/div[3]")
print(html_data[0])

# print(r.text)