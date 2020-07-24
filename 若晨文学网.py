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
        a = a.replace(temp, '')
    # 删除换行的和Tab
    a = a.split('\n')
    start = a.index('')
    end = a.index('\t\t\t')
    a = a[start + 1:end]

    for i in a:
        i = i.replace('\t\t\t\t', '')
        # 用NewList提取
        NewList.append(i)
url1 = 'https://m.ruochenwx.com/85319/p'
url3 = '.html'
#这个根据目录具体有几页来,end为总页数+1
for url2 in range(1,7):
    url2 = str(url2)
    url = url1+url2+url3
    GetCatalog(url)



#进行到这里，NewList内已经存储的是每章的书号名
url1 = 'https://m.ruochenwx.com/85319/'
url4 = '.html'
#页面文字的截取
def GetTxt1(url):
    strhtml = requests.post(url)
    a = strhtml.text
    split = '<div class="content"><p>'
    split = a[0:a.rfind(split, 1)]
    a = a.split(split)
    a = a[1]
    split = '喜欢无法标记（星际）请大家收藏'
    a = a.split(split, 1)[0]

    char = '</p><p>-->>本章未完，点击下一页继续阅读</p><p>'
    if char in a:
        a = a.replace(char, '')
    char = '<p>'
    if char in a:
        a = a.replace(char, '')
    char = '</p>'
    if char in a:
        a = a.replace(char, '')
    char = '<div class="content">'
    if char in a:
        a = a.replace(char, '')
    return  a
index = 0
for url2 in NewList:
    #这个是页数，应该最多就是5页了，根据情况而定，反正多余的处理后也是空值
    for url3 in range(1,6):
        url3 = str(url3)
        url3 = '_'+url3
        url = url1 + url2 + url3 + url4
        temp = GetTxt1(url)
        temp = temp+'\n'
        Nerstr = Nerstr+temp
    index = index+1
    print('第'+str(index)+'章已经加好了')

out = open('C:\\Users\\yjr\\Desktop\\test.txt','w',encoding='utf-8')
out.write(Nerstr)
out.close()
