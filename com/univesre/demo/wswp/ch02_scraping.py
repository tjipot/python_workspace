# -*- coding:utf-8 -*-
# Wswp Chapter 2: 数据抓取(Scraping), 3中抽取网页数据的方法: 1.RegEx, 2.Beautiful Soup, 3.lxml;

# Chapter 2.1, 分析网页: 浏览器 -> View page source -> DOM +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 使用工具: Firebug插件(分析DOM的结构);

# Chapter 2.2, 3种抓取方法: 正则, BS, lxml +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Chapter 2.2.1 Py的RegEx官方: https://docs.python.org/2/howto/regex.html;
import re
import ch01_crawler
def regExDemo():
    # 'http://example.webscraping.com/view/United-Kingdom-239'
    url = 'http://example.webscraping.com/places/default/view/United-Kingdom-239'
    html = ch01_crawler.download(url)
    # <tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>
    re.findall('<tr class="w2p_fw">(.*?)</td>', html)
# 文章中的RegEx还是有脆弱点的;

# Chapter 2.2.2 - BeautifulSoup;
from bs4 import BeautifulSoup
def beautifulSoupDemo():
    '''使用bs4模块, 进行元素提取'''
    broken_html = '<ul class=country><li>Area<li>Population</ul>'
    soup = BeautifulSoup(broken_html, 'html.parser')
    fixed_html = soup.prettify()
    print fixed_html + '\n'

    ul = soup.find('ul', attrs={'class': 'country'})
    # print ul.find('li')  # Returns only the first matched;
    print ul.find_all('li')  # Is A List;
# beautifulSoupDemo()

# 用bs4抓取国家的例子;
def bs4WebScrapDemo():
    url = 'http://example.webscraping.com/places/default/view/United-Kingdom-239'
    html = ch01_crawler.download(url)
    # 如果不写"html.parser": UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser
    # for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a
    # different virtual environment, it may use a different parser and behave differently.
    soup = BeautifulSoup(html, 'html.parser')
    tr = soup.find(attrs={'id':'places_area__row'}) # locate the area row;
    td = tr.find(attrs={'class':'w2p_fw'})          # locate the area tag;
    area = td.text                                  # extract the text from this tag;
    print area
# bs4WebScrapDemo()   # "244,820 square kilometres"

# Chapter 2.2.3 - Lxml: 是libxml2(解析xml的)的Python封装
# import lxml.html
# pip安装lxml未成功: 先跳过[ref: http://lxml.de/installation.html#requirements, https://pypi.python.org/pypi/lxml/3.6.0];
# Source builds on MacOS-X: build instructions, [ref: http://lxml.de/build.html#building-lxml-on-macos-x];




