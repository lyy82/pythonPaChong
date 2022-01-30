# 写数据 write
# fp = open('test.txt','a')
# fp.write('hello world,i am here\n' * 5)
# fp.close()

# 如果再次运行，会先清空原来的数据
# 参数a 是追加

# 读数据
fp = open('test.txt','r')
# 默认情况下read是一字节一字节读，效率比较低
# content = fp.read()
# print(content)

# 一行一行的读取，但是只能读取一行
# content = fp.readline()
# print(content)

# 按照行来读取，会将所以数据都读取到，并且以一个列表返回
content = fp.readlines()
print(content)