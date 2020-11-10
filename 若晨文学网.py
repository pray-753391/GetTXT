import requests
#用它保存书号
NewList = []
#用它保存正文
Nerstr = ''
#获取目录的方法
def GetCatalog(url):
    strhtml = requests.post(url)
    a = strhtml.text

    # 删除无关内容
    split = '<ul class="read">'
    split = a[0:a.rfind(split, 1)]
    a = a.split(split)[1]
    split = '<div class="pagelist">'
    a = a.split(split, 1)[0]
    char = '<ul class="read">'
    if char in a:
        a = a.replace(char, '')
    char = '</ul>'
    if char in a:
        a = a.replace(char, '')
    char = '<li chapter-id="'
    if char in a:
        a = a.replace(char, '')
    a = a.replace(' ', '')

    # 继续删除
    char = '"><ahref="'
    while char in a:
        start = a.find('"><')
        end = a.find('i>')
        temp = a[start:end + 2]
        a = a.replace(temp, ',')

    # 删除换行的和Tab
    a = a.split(',')

    for i in a:
        if i=='':
            continue
        NewList.append(i)

url1 = 'https://m.ruochenwx.com/227832/p'
url3 = '.html'
#这个根据目录具体有几页来,end为总页数+1
for url2 in range(1,6):
    url2 = str(url2)
    url = url1+url2+url3
    GetCatalog(url)

#进行到这里，NewList内已经存储的是每章的书号名
url1 = 'https://m.ruochenwx.com/227832/'
url4 = '.html'
#页面文字的截取
def GetTxt1(url):
    strhtml = requests.post(url)
    a = strhtml.text
    split = '<div class="content"><p>'
    split = a[0:a.rfind(split, 1)]
    a = a.split(split)
    a = a[1]
    split = '喜欢与年下的恋爱法则请大家收藏'
    a = a.split(split, 1)[0]

    char = '</p><p>-->>本章未完，点击下一页继续阅读</p><p>'
    if char in a:
        a = a.replace(char, '')
    char = '<p>'
    if char in a:
        a = a.replace(char, '')
    char = '</p>'
    if char in a:
        a = a.replace(char, '\n')
    char = '<div class="content">'
    if char in a:
        a = a.replace(char, '')
    return  a
index = 1
for url2 in NewList:
    #这个是页数，多的返回temp为''值 根据此判断
    for url3 in range(1,100):
        url3 = str(url3)
        url3 = '_'+url3
        url = url1 + url2 + url3 + url4
        temp = GetTxt1(url)
        if temp == '\n':
            break
        else:
            Nerstr = Nerstr + temp
    Nerstr = Nerstr + '\n' + '第' + str(index) + '章' + '\n'

    print('第'+str(index)+'章已经加好了')
    index = index+1



char = '《与年下的恋爱法则》无错章节将持续在若晨文学小说网更新,站内无任何广告,还请大家收藏和推荐若晨文学！'
if char in Nerstr:
    Nerstr = Nerstr.replace(char,'')
char = '本章未完，请点击下一页继续阅读，后面更精彩！'
if char in Nerstr:
    Nerstr = Nerstr.replace(char,'')

out = open('C:\\Users\\yjr\\Desktop\\test.txt','w',encoding='utf-8')
out.write(Nerstr)
out.close()
