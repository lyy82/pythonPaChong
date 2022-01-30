# 安装xml库
from lxml import etree
# xpath解析
# 1.本地文件
# 2.服务器响应的数据 response.read().decode('utf-8') *****这个用的比较多

# 本地文件 etree.parse
# 服务器响应文件 etree.HTML

tree = etree.parse('070_爬虫_解析_xpath的基本使用.html')
# print(tree)

# xpath 基本语法
# tree.xpath('xpath路径')

# 1.路径查询
# // 查找所有子孙节点
# /  查找子节点
# li_list = tree.xpath('//body/ul/li')
# 判断列表的长度
# print(len(li_list))

# 2.谓词查询
# text()获取标签内容
# li_list = tree.xpath('//ul/li[@id]/text()')
# 找到id为l1的标签，注意引号问题
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')

# 3.属性查询
# 查找到id为l1的li标签的class的属性值
# li_list = tree.xpath('//ul/li[@id="l1"]/@class')

# 4.模糊查询
# 查找id带有l的标签
# li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')
# 查找id以l 开头的li标签
# li_list = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')

# 5.逻辑运算
# 查询id为l1 和class为c1的
li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')

print(li_list)
print(len(li_list))