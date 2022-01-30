# fp = open('text.txt','r')
# fp.read()
# fp.close()

try:
    fp = open('text.txt', 'r')
    fp.read()
except FileNotFoundError:
    print('系统正在升级，请稍后再试...')