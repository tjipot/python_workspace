from bs4 import BeautifulSoup   # 用2to3修改的BeautifulSoup;
import urllib.request           # 原先的urllib2(py2.x), 现在的urllib.request(py3.x);
# from urllib import request
# import urlparse
#########################
# 模块功能: 爬Wikipedia  #
########################

# Helper Fn: 下载某个页面, 以下用法参照源码中的'common.py' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def download5(url, user_agent='wswp', proxy=None, num_retries=2):
    """Download function with support for proxies"""
    print('"download5()" is downloading: ' + url)
    headers = {'User-agent': user_agent}                                    # 设置headers变量;
    request = urllib.request.Request(url, headers=headers)                  # 将headers和url设置进request中;
    # 声明一个opener: The opener will use several default handlers, including support for HTTP, FTP and when applicable, HTTPS;
    opener = urllib.request.build_opener()
    if proxy:
        proxy_params = {urllib.parse.urlparse(url).scheme: proxy}           # proxy参数, {urlparse.urlparse(url).scheme: proxy};
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))       # 给opener添加一个ProxyHandler: 就一种数据结构;
    try:
        html = opener.open(request).read()
    except urllib.request.URLError as e:
        print('Download error: ' + e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = download5(url, user_agent, proxy, num_retries-1)     # 这点破代码, 都用上了递归;
    return html
download = download5                                                        # 绝妙的用法;


# 1.爬取搜索页面(level1 页面), 获取一批(20个)全链接 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import bs4
def linkPageScrap():
    # 把每个页面的link保存, 并依次循环;
    urlSearchPage = 'https://zh.wikipedia.org/w/index.php?cirrusUserTesting=control-explorer-i' \
                    '&search=%E5%8D%A0%E6%98%9F%E6%9C%AF&title=Special:%E6%90%9C%E7%B4%A2&profile=default' \
                    '&fulltext=1&searchToken=477q7t9naiv8bnvdxhf36bohd'
    searchPage = download(urlSearchPage)
    searchSoup = BeautifulSoup(searchPage, 'html.parser')
    # ulEle = searchSoup.find(attrs={'class':'mw-search-results'})            # 搜索ul的;
    ulEle = searchSoup.find_all(attrs={'class':'mw-search-result-heading'})     # 搜索链接div里的<a>的;
    searchedUrlList = []
    searchedUrlNames = []
    baseUrl = 'https://zh.wikipedia.org'

    # 搜索ul的li遍历循环;
    # for child in ulEle.children:
    #     if child.name == 'li':   # li
    #         # print('ulEle: ' + child.name)
    #         # print(child.find('a').get('href'))
    #         print(child)
    #         searchedUrlList.append(baseUrl + child.find('a').get('href'))
    #         searchedUrlNames.append(child.find('a').text)

    # 搜索链接div里的<a>的;
    for item in ulEle:
        searchedUrlList.append(baseUrl + item.find('a').get('href'))        # List添加一个全链接;
    # for item in searchedUrlList:
    #     print(item)
    # for item in searchedUrlNames:
    #     print(item)
    return searchedUrlList
##### 测试:
# theLinks = linkPageScrap()
# print(theLinks)


# 2.爬取单个页面(level2 页面), 获取单独页面的文本内容 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def ctntPageScrap(urlList):                                                                 # 返回urlList中的页面内容
    url02 = 'https://zh.wikipedia.org/wiki/%E5%8D%A0%E6%98%9F%E6%9C%AF'                     # 占星术
    url03 = 'https://zh.wikipedia.org/wiki/%E8%A5%BF%E6%B4%8B%E5%8D%A0%E6%98%9F%E8%A1%93'   # 西洋占星术
    ctntList = []

    # Wiki搜索也是20个结果一页的;
    for eachPage in urlList:
        # wikiHtml = download(url03)
        wikiHtml = download(eachPage)                                                       # 获取页面的HTML内容;
        wikiSoup = BeautifulSoup(wikiHtml, 'html.parser')                                   # 开始解析HTML结果;
        divContent = wikiSoup.find(attrs={'class':'mw-parser-output'})                      # 'mw-parser-output'是内容主体
        # print wikiHtml
        # print type(divContent)  # <class 'bs4.element.Tag'>

        # 分类规则: <h>元素(h2, h3, h4), <p>元素
        textCtnt = '\n'                                                                     # 初始化单页内容文本;
        for child in divContent.children:
            if isinstance(child , bs4.element.Tag):                                         # bs4.element.NavigableString
                # print type(child)
                if child.name == 'p':
                    # print 'In Div'
                    textCtnt += child.text
                    textCtnt += '\n\n'
                elif child.name == 'h2':
                    textCtnt += '##'
                    textCtnt += child.text
                    textCtnt += '\n\n'
                elif child.name == 'h3':
                    # textCtnt += '\t'
                    textCtnt += '###'
                    textCtnt += child.text
                    textCtnt += '\n\n'
                elif child.name == 'h4':
                    textCtnt += '####'
                    textCtnt += child.text
                    textCtnt += '\n\n'
                else:
                    pass
        # print(textCtnt)
        # print('\nAnother Page: ===>>>')
        ctntList.append(textCtnt)
        # for p in divContent.find_all('p'):
        #     # spanText = p.find(attrs={'class':'mw-headline'})
        #     print p.text
    return ctntList
# ctntPageScrap(theLinks)


# 3.将爬到的数据写入到数据库(供调用) ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import pymysql.cursors
import uuid
import time

# 要插入的数据字段: 1.id, 2.name, 3.url, 4.txtCtnt, 5.createtime, 6.comment, 7.numbering;
def insertIntoDb(wsdName='', wsdUrl='', wsdTxtCtnt='', wsdComment='', wsdNumbering=''):
    # 数据组装;
    wsdId = str(uuid.uuid1())
    wsdCreateTime = int(round(time.time() * 1000))

    # 本地测试的connection;
    # connection = pymysql.connect(host='localhost', user='root', password='mastermas', db='wikiScrapDb',
    #                              charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    # 测试环境connection;
    connection = pymysql.connect(host='120.24.47.113', user='xingtu_debug_dba', password='03$TasV#f0h8c', db='xs_app',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `wikiScrapDemo` (`wsd_id`, `wsd_name`, `wsd_url`, `wsd_txtCtnt`, `wsd_createTime`, `wsd_comment`, `wsd_numbering`) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (wsdId, wsdName, wsdUrl, wsdTxtCtnt, wsdCreateTime, wsdComment, wsdNumbering))    # wsdCreateTime隐式转成str了;
            connection.commit()

        # with connection.cursor() as cursor:
        #     # Read a single record
        #     sql = "SELECT * FROM `wikiScrapDemo` WHERE 1 = 1"   # `email`=%s;
        #     # cursor.execute(sql, ('webmaster@python.org',))
        #     cursor.execute(sql)
        #     result = cursor.fetchone()
        #     print(result)
    finally:
        connection.close()


# 4.最终调用数据插入的函数 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def finalInsert():
    theLinks = linkPageScrap()
    ctntList = ctntPageScrap(theLinks)
    for i in range(0, len(theLinks)):
        insertIntoDb(wsdName='NoName', wsdUrl=theLinks[i], wsdTxtCtnt=ctntList[i])

# 5.爬取单个页面 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def ctntPageScrapSingle(url):                                                               # 返回urlList中的页面内容
    url02 = 'https://zh.wikipedia.org/wiki/%E5%8D%A0%E6%98%9F%E6%9C%AF'                     # 占星术
    url03 = 'https://zh.wikipedia.org/wiki/%E8%A5%BF%E6%B4%8B%E5%8D%A0%E6%98%9F%E8%A1%93'   # 西洋占星术

    # Wiki搜索也是20个结果一页的;
    wikiHtml = download(url)                                                       # 获取页面的HTML内容;
    wikiSoup = BeautifulSoup(wikiHtml, 'html.parser')                                   # 开始解析HTML结果;
    # 初始化抓取内容;# 初始化单页内容文本;
    textCtnt = '\n'
    # 1.抓取'h1'内容;
    h1Content = wikiSoup.find(attrs={'class':'firstHeading'})
    textCtnt += '一级标题: '
    textCtnt += h1Content.text
    # 2.抓取主题内容;
    divContent = wikiSoup.find(attrs={'class':'mw-parser-output'})                      # 'mw-parser-output'是内容主体
    # print wikiHtml
    # print type(divContent)  # <class 'bs4.element.Tag'>

    # 分类规则: <h>元素(h2, h3, h4), <p>元素
    return horizontalTraverser(divContent, textCtnt)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def horizontalTraverser(parentTag, scrawlContent):
    # print('ABC: ', parentTag.text)    # 简单粗暴的方法;
    for childTag in parentTag.children:            # .children是纵向遍历, 下面的if else是横向遍历;
        if isinstance(childTag , bs4.element.Tag): # bs4.element.NavigableString
            if childTag.name == 'p':               # 需处理的元素类型(内容div下): p, h2, h3, h4, ul, 不处理: div;
                scrawlContent += '\n'
                scrawlContent += childTag.text
            elif childTag.name == 'h1':
                scrawlContent += '\n\n\n\n\n'
                scrawlContent += '一级标题: '
                scrawlContent += childTag.text
            elif childTag.name == 'h2':
                scrawlContent += '\n\n\n\n'
                scrawlContent += '二级标题: '     # '##'
                scrawlContent += childTag.text
            elif childTag.name == 'h3':
                scrawlContent += '\n\n\n'
                scrawlContent += '三级标题: '     # '###'
                scrawlContent += childTag.text
            elif childTag.name == 'h4':
                scrawlContent += '\n\n'
                scrawlContent += '四级标题: '     # '####'
                scrawlContent += childTag.text
            elif childTag.name == 'blockquote':
                # print('blockquote', childTag)
                # for blockquoteChild in childTag:
                scrawlContent += '\n'
                scrawlContent += '以下是引用: '  # '####'
                scrawlContent += childTag.text
            elif childTag.name == 'dl':
                scrawlContent += '\n'
                scrawlContent += childTag.text
            elif childTag.name == 'table':
                scrawlContent += '\n\n'
                scrawlContent += '以下是表格内容: '  # '####'
                scrawlContent += childTag.text
            elif childTag.name == 'ul' or childTag.name == 'ol': # div下ul处理逻辑: 提取ul直接包括的元素li下的第一子集: b或a或p;
                # print(child.children)
                try:
                    for liEle in childTag.children:
                        if liEle.name == 'li':
                            scrawlContent += '\n\t'
                            scrawlContent += liEle.text     # print(liEle.text), 即可以提取li下面的所有text文本: 简单干脆!
                            scrawlContent += ' '
                except:
                    print('发生了Error!')
            else:
                pass
    return scrawlContent

# horizontalTraverser的备份 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def horizontalTraverserBak(parentTag, scrawlContent):
    print('ABC: ', parentTag.text)
    for childTag in parentTag.children:            # .children是纵向遍历, 下面的if else是横向遍历;
        if isinstance(childTag , bs4.element.Tag): # bs4.element.NavigableString
            if childTag.name == 'p':               # 需处理的元素类型(内容div下): p, h2, h3, h4, ul, 不处理: div;
                scrawlContent += '\n'
                scrawlContent += childTag.text
            elif childTag.name == 'h1':
                scrawlContent += '\n\n\n\n\n'
                scrawlContent += '一级标题: '
                scrawlContent += childTag.text
            elif childTag.name == 'h2':
                scrawlContent += '\n\n\n\n'
                scrawlContent += '二级标题: '     # '##'
                scrawlContent += childTag.text
            elif childTag.name == 'h3':
                scrawlContent += '\n\n\n'
                scrawlContent += '三级标题: '     # '###'
                scrawlContent += childTag.text
            elif childTag.name == 'h4':
                scrawlContent += '\n\n'
                scrawlContent += '四级标题: '     # '####'
                scrawlContent += childTag.text
            elif childTag.name == 'ul' or childTag.name == 'ol': # div下ul处理逻辑: 提取ul直接包括的元素li下的第一子集: b或a或p;
                # print(child.children)
                try:
                    for liEle in childTag.children:
                        if liEle.name == 'li':
                            scrawlContent += '\n\t'
                            scrawlContent += liEle.text     # print(liEle.text), 即可以提取li下面的所有text文本: 简单干脆!
                            scrawlContent += ' '
                            # print(liEle.name)           # liEle.name = 本名或'None'
                            # if isinstance(liEle, bs4.element.Tag):    # 提取出ul的li, 排除'\n';
                            # Seperater分隔 ++++++++++++++++++++++++++++++++++++++++++++++++++++
                            # tmpIndex = 0                            # 每一个li元素, 重置;
                            # for liFirstChildEle in liEle:
                            #     print(liFirstChildEle.text)
                            #     scrawlContent += '\n'
                            #     scrawlContent += liFirstChildEle.text
                            #     scrawlContent += ' '
                            #     tmpIndex += 1
                            #     if tmpIndex != 0:
                            #         break
                except:
                    print('发生了Error!')
                    # 省略: 参考文献, 外部链接;
                    # liFirstChildEle = liEle.children    # .__getitem__(0)
                    # print(liFirstChildEle)
                    # if liFirstChildEle.__next__().name == 'b' or liFirstChildEle.__next__().name == 'a':
                    #     print(liFirstChildEle.__next__().text)
            else:
                pass
    return scrawlContent

def singlePageInsert(): # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -- Method 01;
    # urlName = '天王星'
    # urlUrl  = 'https://zh.wikipedia.org/wiki/%E5%A4%A9%E7%8E%8B%E6%98%9F'
    # -- Method 02;
    # urlFromExcel = "天狼星	https://zh.wikipedia.org/wiki/%E5%A4%A9%E7%8B%BC%E6%98%9F"
    # urlName, urlUrl = urlFromExcel.split("\t")
    # -- Method 03;
    tupleEntries = readEntriesFromFile("/Users/UNIVESRE/Desktop/有异常的链接合辑.TXT")
    for eachTuple in tupleEntries:
        numbering, name, url, comment = eachTuple
        ctnt = '无对应网页'
        if url != '无':              # 有对应的网页, 需爬, 再插入到数据库;
            ctnt = ctntPageScrapSingle(url)
        try:
            pass
            # insertIntoDb(wsdName=name, wsdUrl=url, wsdTxtCtnt=ctnt, wsdComment=comment, wsdNumbering=numbering)
        except:
            print("##### 文件'", numbering, "'有异常字符!")
        finally:
            pass
        # 微处理下文件名: 在文件名最前面添加'numbering'的数字部分;
        numberPart = numbering[:-3:-1]  # 逆序获取最后两位: 'TAROT01' -> '10';
        numberPart = numberPart[::-1]   # 翻转字符串: '10' -> '01';
        fileName = numberPart + name    # 拼接: 数字部分 + 名称部分;
        createTxtFile(fileName, ctnt)   # 生成文件;


# Helper Fn ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def createTxtFile(fileName, fileContent):
    with open("/Users/UNIVESRE/Desktop/%s.TXT"%fileName, "w") as f:
        f.write(fileContent)
    print(fileName, "File Written!")


# Helper Fn ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def readEntriesFromFile(fileName):
    urlTupleEntries = []
    for line in open(fileName):
        lineWithoutRowBreak = line.replace('\n', '')   # 行尾有一个'\n', 提取之后只剩一个元素
        numbering, name, url, comment = lineWithoutRowBreak.split('\t')
        lineTuple = (numbering, name, url, comment)
        urlTupleEntries.append(lineTuple)
    # 返回一个(元组)数组;
    return urlTupleEntries


# End: 模块完成, 调用运行 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# finalInsert()     # 从搜索页面开始插入数据库;
# readEntriesFromFile("/Users/UNIVESRE/Desktop/02塔罗.TXT")
singlePageInsert()  # 单独一个页面插入数据;
