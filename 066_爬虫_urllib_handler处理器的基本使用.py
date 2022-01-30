# 请求头  每次登录Cookie不一样，就需要用handler定制更高级的请求头 还有代理

import urllib.request

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

# handler build_opener open

# 1.获取handler对象
handler = urllib.request.HTTPHandler
# 2.获取opener对象
opener = urllib.request.build_opener(handler)
# 3.调取open方法
response = opener.open(request)

content = response.read().decode('utf-8')
print(content)