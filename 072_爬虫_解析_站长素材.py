# 需求 下载的前十页的图片
# https://sc.chinaz.com/tupian/qinglvtupian.html
# https://sc.chinaz.com/tupian/qinglvtupian_2.html
# https://sc.chinaz.com/tupian/qinglvtupian_3.html


import urllib.request
from lxml import etree


def creat_request(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    # 下载图片
    #     urllib.request.urlretrieve('图片地址', '文件名字')
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@id="container"]//a/img/@alt')
    # 一般设计到图片的网站，都会进行懒加载
    src_list = tree.xpath('//div[@id="container"]//a/img/@src2')

    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src

        urllib.request.urlretrieve(url=url, filename='./loveImg/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))

    for page in range(start_page, end_page + 1):
        # 请求对象定制
        request = creat_request(page)
        # 获取网页的源码
        content = get_content(request)
        # 下载
        down_load(content)
