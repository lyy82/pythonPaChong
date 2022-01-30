# 序列化-->内存中的数据变成字节序列
# fp = open('test.txt','w')
# # 默认情况下我们只能将字符串写入
# fp.write('hello world')
# fp.close()

# fp = open('test.txt','w')
# name_list = ['zhangsan','lisi']
# fp.write(name_list)

# dumps()
# fp = open('test.txt','w')
# name_list = ['zhangsan','lisi']
# # 导入到json模块到该文件中
# import json
# # 序列化
# # 我们在使用scrapy框架的时候该框架会返回一个对象
# names = json.dumps(name_list)
# fp.write(names)
# fp.close()

# dump
# 在将对象转换为字符串的同时，指定一个文件的对象

# fp = p = open('test.txt','w')
# name_list = ['zhangsan','lisi']
# import json
# json.dump(name_list,fp)

# 反序列化 load,loads
# fp = open('test.txt','r')
# content = fp.read()
# import json
# result = json.loads(content)
# print(result)

fp = open('test.txt','r')
import json
result = json.load(fp)

fp.close()
