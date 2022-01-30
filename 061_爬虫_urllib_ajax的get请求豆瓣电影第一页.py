# get请求
# 获得豆瓣电影的第一页数据 并且保存

import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=40&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 数据下载到本地
# open方法默认使用的gbk编码，如果我们想要保存汉字，utf-8 需要指定
# fp = open('douban.json','w',encoding='utf-8')
# fp.write(content)
with open('douban1.json','w',encoding='utf-8') as fp:
    fp.write(content)
