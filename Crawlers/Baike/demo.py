import urllib.request
import urllib.error

# urlopen方法
response = urllib.request.urlopen('https://www.baidu.com/')
print('Status Code:', response.getcode())
html = response.read().decode('utf8')
print(html)

# headers信息
headers = {'User-Agent': 'Chrome/67.0.3396.99'}
request = urllib.request.Request('https://www.baidu.com/', headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf8')
print('Full Page:', len(html))

# error的使用
try:
    urllib.request.urlopen('https://www.google.com/', timeout=0.5)
except urllib.error.HTTPError as e:
    print('HTTPError:', e.code)
except urllib.error.URLError as e:
    print('URLError:', e.reason)
else:
    print('You used a proxy')
