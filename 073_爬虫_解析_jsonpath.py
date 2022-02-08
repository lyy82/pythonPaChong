import json
import jsonpath

obj = json.load(open('073_爬虫_解析_jsonpath.json', 'r', encoding='utf-8'))
# 书店所有的书的作者

# author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
# author_list = jsonpath.jsonpath(obj, '$.store.book[0].author')
# print(author_list)

# 所有的作者
# author_list = jsonpath.jsonpath(obj, '$.store..author')
# print(author_list)

# store下面的所有的元素
# tag_list = jsonpath.jsonpath(obj, '$.store.*')
# print(tag_list)

# 第二本书
# book = jsonpath.jsonpath(obj, '$.store.book[1]')
# print(book)

# 最后一本书
# book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# print(book)
# 前两本书
# book_list = jsonpath.jsonpath(obj, '$..book[0,1]')
# book_list = jsonpath.jsonpath(obj, '$..book[:2]')
# print(book_list)

# 条件过滤需要在()添加一个?
# 过滤出所有有 author 的书
# book_list = jsonpath.jsonpath(obj, '$..book[?(@.title)]')
# print(book_list)

# 那本书超过了10块钱
# book_list = jsonpath.jsonpath(obj, '$..book[?(@.price > 10)]')
# print(book_list)
