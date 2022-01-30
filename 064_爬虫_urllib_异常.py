# URLError/HTTPError
import urllib.request
import urllib.error

# url = 'https://blog.csdn.net/m0_45432976/article/details/1220205711'

url = 'http://www.goudan111.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

try:
    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print('系统正在升级...')
except urllib.error.URLError:
    print('不存在的网路地址')