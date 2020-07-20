import requests
r = requests.get('https://www.993dy.com/vod-detail-id-10549.html')
r.encoding('utf8')
print(r.text)