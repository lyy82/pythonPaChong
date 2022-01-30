import urllib.request

# 下载一个网页
# url_page = 'http://www.baidu.com'
# url代表下载路径，filename 文件名字
# 在python中 可以写变量的名字 也可以直接写值
# urllib.request.urlretrieve(url_page,'baidu.html')


# 下载图片
# url_img = 'https://img0.baidu.com/it/u=2312007843,1698221019&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=823'
#
# urllib.request.urlretrieve(url_img,filename='lisa.jpg')

# 下载视频
url_video = 'https://vd3.bdstatic.com/mda-naj30kx43e4g7u0q/sc/cae_h264_nowatermark_delogo/1642644806842325002/mda-naj30kx43e4g7u0q.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1642690790-0-0-ef8ca0e28193e813898fe68c9faf8b41&bcevod_channel=searchbox_feed&pd=1&pt=3&logid=1790720328&vid=11981634055924625534&abtest=&klogid=1790720328'
urllib.request.urlretrieve(url_video,'chaoxian.mp4')