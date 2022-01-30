# 适用的场景：在数据采集的时候 需要绕过登录 进入到某个页面
# 个人信息页面是utf-8 但是还是报错了编码错误
# 因为没有进入到个人信息页面，进入登录页面 登录页面不是utf-8

# 什么情况下访问不成功，请求头信息不够

import urllib.request

url = 'https://weibo.cn/651491586/info'

headers = {
    # cookie中携带着你的登录信息，如果有登录之后的cookie 那么可以携带着cookie进入页面
    # referer 判断当前路径是不是由上一个路径进来的，一般情况下是做图片的防盗链
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

# 请求定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取页面内容
content = response.read().decode('gb2312')

# 将数据保存在本地
with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)