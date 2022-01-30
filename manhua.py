import requests, re
from bs4 import BeautifulSoup
import bs4
import os
import urllib

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'referer': 'https://www.fffdm.com/',
    'cookie': "picHost=p5.fzacg.com; Hm_lvt_cb51090e9c10cda176f81a7fa92c3dfc=1545054252,1545054291,1545054381,1545054404; Hm_lpvt_cb51090e9c10cda176f81a7fa92c3dfc=1545054475"
}

def getHTML(url):
    try:
        r = requests.get(url,headers = headers, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except requests.exceptions.HTTPError as e:
        return 0

def fillNeedInfo(url, html):
    text = html.text
    needText = re.findall('var mhurl = "(.*?)"',text)

    needText = needText[0]

    return needText
def saveInfo(picUrl, picPath, chapter, page):
    picClass = picUrl.split('.')[-1]
    if picClass == 'jpg':
        try:
            req = urllib.request.Request(picUrl, headers=headers)
            data = urllib.request.urlopen(req,timeout = 300).read()
            with open(picPath+'/'+str(page)+'.jpg', 'wb') as f:
                f.write(data)
                f.close()
            print('第' + str(chapter) + '章第' + str(page) + '页爬取成功')
        except Exception as e:
            print(str(e))
    elif picClass == 'png':
        try:
            req = urllib.request.Request(picUrl, headers=headers)
            data = urllib.request.urlopen(req).read()
            with open(picPath+'/'+str(page)+'.png', 'wb') as f:
                f.write(data)
                f.close()
            print('第' + str(chapter) + '章第' + str(page) + '页爬取成功')
        except Exception as e:
            print(str(e))

def updataUrl(url, chapter, page):
    url += str(chapter)

    url += '/index_'

    url += str(page)

    url += '.html'
    print(url)
    return url

def getChapterNum(url):
    text = getHTML(url).text
    chapterNumList = re.findall('a href="(.*?)/" title="(.*?)"',text)
    chapterNumList.pop(0)
    return chapterNumList

exceptionList = []

def reptileMain(url):
    leftPictureUrl = "https://p5.fzacg.com/"

    try:            #创建文件夹存放
        os.mkdir('image')
    except:
        pass

    chapterNumList = getChapterNum(url)     #章节列表

    page = 0        #页码标记

    star = 1
    for chapterNum in chapterNumList:
        page = 0
        picPath = 'image/' + str(chapterNum[1])      #章节文件路径

        for value in range(0,500):          #单章最多500页
            try:
                html = getHTML(updataUrl(url,chapterNum[0],page))   #获取页面信息
                if html == 0:           #若404则html=0,此时跳出循环  page超出页数
                    break

                pictureUrl = leftPictureUrl + fillNeedInfo(url, html)

                try:        #为每章创建目录
                    os.mkdir(picPath)
                except Exception as e:
                    pass
                saveInfo(pictureUrl, picPath, chapterNum[0], page)

            except Exception as e:
                exceptionList.append(e) #记录错误信息
            page += 1
            for value in range(0,star):
                print('*',end='')
            print(' ')
            star += 3
            if star > 35:
                star = 1

def main():
    url = input("请输入风之动漫漫画目录网址：")
    print('开始爬取，爬取文件将新建文件目录image,如果已经存在，请注意文件存放')
    reptileMain(url)
    print('爬取成功')
main()
print('程序出现以下错误：')
for value in exceptionList:
    print(value)

over = input("程序运行结束，请敲回车结束或之间关闭")

