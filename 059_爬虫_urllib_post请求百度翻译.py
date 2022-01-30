# post请求
import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

data = {
    'kw':'spider'
}

# post请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post的请求参数 是不会拼接在url后面的，放在请求对象定制的参数中
# post请求的参数 必须进行编码
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 字符串--》json对象
import json
obj = json.loads(content)
print(obj)

# post请求方式的参数 必须编码
# 编码之后 必须调用encode方法
# 参数是放在请求对象定制的方法中