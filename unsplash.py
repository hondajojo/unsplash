#!/usr/bin/python2
#coding=utf-8
#下载unsplash.com的图片
import re
import urllib2
import urllib
import itertools
page = int(raw_input('input the page you want to download:'))
url = 'http://unsplash.com/?page=%d'%page

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.102 Safari/537.36'}
req = urllib2.Request(url,headers=headers)
html = urllib2.urlopen(req).read()

s = r'src="(.*?)"\sclass' #图片的正则i
picurl = re.findall(s,html) #匹配图片的链接
l = 1
r = []
for i in picurl:
    p = i.split('amp;')  #去除图片图片链接里的amp;
    w = ''.join(itertools.chain(*p)) #将一个列表里的元素合并为一个字符串
    t = w.split('https://')
    y = ''.join(itertools.chain(*t))
    r.append(y)
m = []
for k in r:
    e = 'http://'+k
    m.append(e)

for g in m:
    urllib.urlretrieve(g,'%d.jpg'%l)
    l += 1
