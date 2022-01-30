
import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)

proxies ={
    'http':'60.250.159.191:45983'
}

handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

# 获取响应信息
content = response.read().decode('utf-8')
with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(content)