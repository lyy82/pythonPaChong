import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

# 一个类型和六个方法
# <class 'http.client.HTTPResponse'>

# 按照一个字节一个字节的去读
content = response.read()
# print(content)

# 返回多少个字节
# content = response.read(5)
# print(content)

# 读取一行
content = response.readline()
# print(content)

content = response.readlines()
# print(content)

# 返回状态码 如果是200了，那么就证明我们逻辑没有错
print(response.getcode())

# 返回的是url地址
print(response.geturl())

# 返回的状态信息
print(response.getheaders())