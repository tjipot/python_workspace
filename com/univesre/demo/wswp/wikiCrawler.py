# import ch01_crawler
from bs4 import BeautifulSoup
import urllib.request   # 原先的urllib2
# import urlparse
# from urllib import request

# 以下用法参照源码中的'common.py';
def download5(url, user_agent='wswp', proxy=None, num_retries=2):
    """Download function with support for proxies"""
    print('Downloading: ' + url)
    headers = {'User-agent': user_agent}                            # 设置headers变量;
    request = urllib.request.Request(url, headers=headers)                 # 将headers和url设置进request中;
    # 声明一个opener: The opener will use several default handlers, including support for HTTP, FTP and when applicable, HTTPS;
    opener = urllib.request.build_opener()
    if proxy:
        proxy_params = {urllib.parse.urlparse(url).scheme: proxy}       # proxy参数, {urlparse.urlparse(url).scheme: proxy};
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))      # 给opener添加一个ProxyHandler: 就一种数据结构;
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

download = download5


## 爬Wikipedia;
import bs4
# 爬取搜索页面(level1 页面)
def linkPageScrap():
    # 把每个页面的link保存, 并依次循环;
    urlSearchPage = 'https://zh.wikipedia.org/w/index.php?cirrusUserTesting=control-explorer-i&search=%E5%8D%A0%E6%98%9F%E6%9C%AF&title=Special:%E6%90%9C%E7%B4%A2&profile=default&fulltext=1&searchToken=477q7t9naiv8bnvdxhf36bohd'
    searchPage = download(urlSearchPage)
    searchSoup = BeautifulSoup(searchPage, 'html.parser')
    ulEle = searchSoup.find(attrs={'class':'mw-search-results'})



# 爬取单个页面(level2 页面)
def wikiPediaDemo():
    url01 = 'https://zh.wikipedia.org/w/index.php?cirrusUserTesting=control-explorer-i&search=%E5%8D%A0%E6%98%9F%E6%9C%AF&title=Special:%E6%90%9C%E7%B4%A2&profile=default&fulltext=1&searchToken=477q7t9naiv8bnvdxhf36bohd'
    url02 = 'https://zh.wikipedia.org/wiki/%E5%8D%A0%E6%98%9F%E6%9C%AF'                     # 占星术
    url03 = 'https://zh.wikipedia.org/wiki/%E8%A5%BF%E6%B4%8B%E5%8D%A0%E6%98%9F%E8%A1%93'   # 西洋占星术

    wikiHtml = download(url03)

    wikiSoup = BeautifulSoup(wikiHtml, 'html.parser')
    divContent = wikiSoup.find(attrs={'class':'mw-parser-output'})
    # print wikiHtml
    # print wikiTr
    # print type(divContent)  # <class 'bs4.element.Tag'>

    # 分类规则: <h>元素(h234), <p>元素
    content01 = '\n'
    for child in divContent.children:
        if isinstance(child , bs4.element.Tag): # bs4.element.NavigableString
            # print type(child)
            if child.name == 'p':
                # print 'In Div'
                content01 += child.text
                content01 += '\n\n'
            elif child.name == 'h2':
                content01 += '##'
                content01 += child.text
                content01 += '\n\n'
            elif child.name == 'h3':
                # content01 += '\t'
                content01 += '###'
                content01 += child.text
                content01 += '\n\n'
            elif child.name == 'h4':
                content01 += '####'
                content01 += child.text
                content01 += '\n\n'
            else:
                pass
            # print child.name
            # print '##########+End'

    print(content01)

        # pass
        # print child
        # print type(child)
        # if child  :
        #     print 'div'


        # if child.find('p'):
        #     print 'p'
        # elif child.find('h2'):
        #     print 'h2'
        # elif child.find('table'):
        #     print 'table'
        # else:
        #     print 'Others'

    # for p in divContent.find_all('p'):
    #     # spanText = p.find(attrs={'class':'mw-headline'})
    #     #
    #     print p.text

wikiPediaDemo()