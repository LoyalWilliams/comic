#coding=utf-8
import spiders
from comicspider.spiders import manhua163Spider,shenmanhuaSpider,tencentSpider
def getSpider(url):
    if '163.bilibili.com' in url:
        return manhua163Spider.manhua163
    elif 'www.shenmanhua.com' in url:
        # print 1
        return shenmanhuaSpider.shenmanhua
    elif 'ac.qq.com' in url:
        # print 1
        return tencentSpider.tencentSpider
