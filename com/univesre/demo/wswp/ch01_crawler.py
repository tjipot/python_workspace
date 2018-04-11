# -*- coding: utf-8 -*-
# /System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7            -命令
# /Users/UNIVESRE/Documents/workspace_python/com/univesre/demo/wswp/ch01_crawler.py  -参数(文件)

# WSWP Chapter 1.4.1, 下载网页 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# The urllib2 module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world - basic
# and digest authentication, redirections, cookies and more.
import urllib2

def download(url, user_agent='wswp', num_retries=2):
    print 'Downloading: ', url
    headers = {'User-agent': user_agent}                    # 3.设置用户代理
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()              # urlopen参数可以是url以及request
    except urllib2.URLError as e:                           # 1.添加URLError异常处理
        print 'Download error: ', e.reason
        html = None
        if num_retries > 0:                                 # 2.添加下载重试代码
            if hasattr(e, 'code') and 500 <= e.code < 600:  # 'code'应是e对象的属性之一
                # Recursively retry 5xx HTTP errors
                return download(url, user_agent, num_retries-1)
    return html                                             # urllib2.urlopen(url).read()

url01 = "https://www.baidu.com"
url02 = "http://httpstat.us/500"    # 始终返回500响应码
''' Downloading:  http://httpstat.us/500
    Download error:  Internal Server Error
    Downloading:  http://httpstat.us/500
    Download error:  Internal Server Error
    Downloading:  http://httpstat.us/500
    Download error:  Internal Server Error
    Result:  None   '''
# tmpHtml = download(url02)
# print 'Result: ', tmpHtml

# 以下用法参照源码中的'common.py';
def download5(url, user_agent='wswp', proxy=None, num_retries=2):
    """Download function with support for proxies"""
    print 'Downloading: ', url
    headers = {'User-agent': user_agent}                            # 设置headers变量;
    request = urllib2.Request(url, headers=headers)                 # 将headers和url设置进request中;
    # 声明一个opener: The opener will use several default handlers, including support for HTTP, FTP and when applicable, HTTPS;
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}       # proxy参数;
        opener.add_handler(urllib2.ProxyHandler(proxy_params))      # 给opener添加一个ProxyHandler: 就一种数据结构;
    try:
        html = opener.open(request).read()
    except urllib2.URLError as e:
        print 'Download error: ', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = download5(url, user_agent, proxy, num_retries-1)     # 这点破代码, 都用上了递归;
    return html

download = download5    # 像个'替身';


# WSWP Chapter 1.4.2, 网站地图(robots.txt)爬虫, 需依赖Sitemap文件 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import re
def crawl_sitemap(url):
    sitemap = download(url)                             # download sitemap file
    links = re.findall('<loc>(.*?)</loc>', sitemap)     # extract sitemap links
    print links
    for link in links:
        html = download(link)                           # download each link
        # scrape html here...
        print html

# crawl_sitemap('http://example.webscraping.com/sitemap.xml')
""" Downloading:  http://example.webscraping.com/sitemap.xml
    []  """


# WSWP Chapter 1.4.3, 后缀ID遍历爬虫, 需要结构有一定规律 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import itertools    # 9.7. itertools — Functions creating iterators for efficient looping

def id_crawler(max_errors = 5, num_errors = 0):
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-%d' % page
        html = download(url)
        if html is None:
            num_errors += 1     # Received an error when downloading the webpage
            if num_errors == max_errors:
                break           # reached maximum number of consecutive errors
        else:
            # success: can scrape the result
            # pass
            print html
            num_errors = 0
# 运行一遍
# id_crawler()

# ####
# WSWP Chapter 1.4.4, 链接爬虫, 使用链接的爬虫方式更加符合用户Style, 但也更复杂 +++++++++++++++++++++++++++++++++++++++++++++++
import re
import urlparse

# Crawl from the given seed URL following links matched by link_regex
def link_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)         # Keep track which URL's have seen before;
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        # print 'After Download...'
        # print html
        # filter for links matching our regular expression
        # ['/places/default/index', '#', '/places/default/user/register?_next=/places/default/index',
        # '/places/default/user/login?_next=/places/default/index', '/places/default/index', '/places/default/search',
        # '/places/default/view/Afghanistan-1', '/places/default/view/Aland-Islands-2', '/places/default/view/Albania-3',
        # '/places/default/view/Algeria-4', '/places/default/view/American-Samoa-5', '/places/default/view/Andorra-6',
        # '/places/default/view/Angola-7', '/places/default/view/Anguilla-8', '/places/default/view/Antarctica-9',
        # '/places/default/view/Antigua-and-Barbuda-10', '/places/default/index/1']
        for link in get_links(html):
            # print link
            # print get_links(html)
            if re.match(link_regex, link):                  # Check if link matches expected regex;
                # print 'PlaceholderX'
                # print link
                link = urlparse.urljoin(seed_url, link)     # 由相对路径Join成绝对路径;
                if link not in seen:                        # Check if link is already in 'seen';
                    seen.add(link)
                    crawl_queue.append(link)

# Return a list of links from html
def get_links(html):
    # A regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # print webpage_regex
    # List of all links from the webpage
    return webpage_regex.findall(html)

# 我要让书上的下载错误出现的: 按照书上写的'/(index|view)', 永远进不了打印'PlaceholderX'的if条件体内, 关键是要'*', r可以不要;
# link_crawler('http://example.webscraping.com', r'/(index|view)*')

## 高级功能: 使用robotparser, 解析robots.txt, 以免去爬了不能爬的那些URL, 可以将该功能添加到link_crawler()中 --------------------
import robotparser
def robots_parser():
    rp = robotparser.RobotFileParser()
    rp.set_url('http://example.webscraping.com/robots.txt')
    rp.read()
    url = 'http://example.webscraping.com'
    user_agent01 = 'BadCrawler'             # True
    print rp.can_fetch(user_agent01, url)
    user_agent02 = 'GoodCrawler'            # True
    print rp.can_fetch(user_agent02, url)
# 运行:
# robots_parser()

## 代理支持(略): 用代理(即某台中间的服务器)去访问某个网站, 如Netflix屏蔽了美国以外的大多数国家, -----------------------------------
# 可以用urllib2或者Py Http模块的requests;

## 下载限速: 通过间隔时间的方式 --------------------------------------------------------------------------------------------
import datetime
import time
class Throttle:
    '''Add a delay between downloads to the same domain'''
    def __init__(self, delay):  # Throttle的初始化函数;
        self.delay = delay
        self.domains = {}

    def wait(self, url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                # domain has been accessed recently, so need to sleep
                time.sleep(sleep_secs)
        # update the last accessed time
        self.domains[domain] = datetime.datetime.now()
# 运行:
delay = 1000        # 这个值应该是0.001秒;
throttle = Throttle(delay)    # print datetime.datetime.now(): 2018-04-09 17:15:58.539840
# ...   # 中间爬取的代码;
delayUrl = 'http://example.webscraping.com'
throttle.wait(delayUrl)
# result = download(delayUrl, 'wswp', num_retries=3)   # proxy: 见'代理支持';
# print datetime.datetime.now()
# print datetime.datetime.now().second - datetime.datetime.now().second
# print datetime.datetime.now().microsecond


## 避免爬虫陷阱: 略 ------------------------------------------------------------------------------------------------------

## 最终版本: 略 ---------------------------------------------------------------------------------------------------------

