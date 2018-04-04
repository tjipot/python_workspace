#-*- coding:utf-8 -*-
import urllib2
from   bs4 import BeautifulSoup
import re
import random
import datetime
# ref: https://blog.csdn.net/u014518506/article/details/53436549;

random.seed(datetime.datetime.now())

def getLink(url):
    html  = urllib2.urlopen("http://en.wikipedia.org" + url)
    bsObj = BeautifulSoup(html, 'html.parser')
    return bsObj.find('div', id="bodyContent").find_all('a', href=re.compile("^(/wiki/)((?!;)\S)*$"))

url   = "/wiki/Kevin_Bacon"
file  = open("wiki.txt", "w")
links = getLink(url)
while len(links)>0:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    file.write(newArticle + "\n")
    print newArticle
    links = getLink(newArticle)
file.close()
