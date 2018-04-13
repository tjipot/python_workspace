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
    print('download5() downloading:' + url)
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

# 要插入的数据字段: 1.id, 2.name, 3.url, 4.txtCtnt, 5.createtime;
def insertIntoDb(wsdName='', wsdUrl='', wsdTxtCtnt=''):
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
            sql = "INSERT INTO `wikiScrapDemo` (`wsd_id`, `wsd_name`, `wsd_url`, `wsd_txtCtnt`, `wsd_createTime`) " \
                  "VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (wsdId, wsdName, wsdUrl, wsdTxtCtnt, wsdCreateTime))    # wsdCreateTime隐式转成str了;
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

# End: 模块完成, 调用运行:
finalInsert()


import sys
