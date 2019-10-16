#coding=utf-8
import json
import re

import requests
from lxml import etree

import comicspider.settings


class defaultSpider():
    def __init__(self,url):
        self.url=url
        self.rule= comicspider.settings.getRule(url)

    def getSourceCode(self,url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
            }
        response = requests.get(url, headers=headers, verify=False).content
        return response

    def getChapters(self,url):
        headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
           }
        sourceCode=self.getSourceCode(url)
        selector=etree.HTML(sourceCode)
        comicName = selector.xpath("//div[contains(@class,'header')]//h1/text()")[0]
        bookId = url[url.rindex('/')+1:]
        url='https://163.bilibili.com/book/catalog/'+bookId
        response=requests.get(url,headers=headers,verify=False).content
        sections=json.loads(response)['catalog']['sections'][0]['sections']
        chapters=[]
        for each in sections:
            sectionId=each['sectionId']
            title=each['fullTitle']
            chapterUrl='https://163.bilibili.com/reader/'+bookId+"/"+sectionId
            content={'comicName':comicName,'sectionId':sectionId,'title':title,'chapterUrl':chapterUrl}
            chapters.append(content)
        return chapters

    def getContent(self,url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
            }
        response = requests.get(url, headers=headers, verify=False).content
        pattern = re.compile(r'url: window.IS_SUPPORT_WEBP [?](.*)')
        imgUrls = pattern.findall(response)
        l=[]
        for each in imgUrls:
            imgUrl=each.replace('\"', '').rstrip(',').strip()
            imgUrl=imgUrl.split(' : ')
            pattern = re.compile(r'NOSAccessKeyId=(.*)')
            imgUrl=[re.sub(pattern, 'NOSAccessKeyId=c92f74b0d48f4fb39271a1109da74cc2', a).replace(' ','') for a in imgUrl]
            # print re.sub(pattern, 'NOSAccessKeyId=c92f74b0d48f4fb39271a1109da74cc2', imgUrl)
            l.append(imgUrl)
        return l

    def getInfoUrlByChapterUrl(self,chapterUrl):
        rindex1=chapterUrl.rindex('/')
        url=chapterUrl[0:rindex1]
        key=url[url.rindex('/')+1:]
        return 'https://163.bilibili.com/source/'+key

    # def getComics(self):
    #     jtext=self.getSourceCode('https://163.bilibili.com/category/getData.json?sort=2&sf=1&pageSize=72&page=1')
    #     books=json.loads(jtext)['books']
    #     for book in books:
    #         cover = book['cover']
    #         author=book['author']
    #         title=book['title']

    def getRecommend(self):
        recommendsText = self.getSourceCode('https://h5.manhua.163.com/reader/recommend/layer.json')
        recommends=json.loads(recommendsText)['recommends']
        recommends[0]['url']='https://163.bilibili.com/source/'+recommends[0]['targetId']
        for recommend in recommends:
            recommend['url'] = 'https://163.bilibili.com/source/' + recommend['targetId']
        return recommends

class shenmanhuaSpider(defaultSpider):
    def getChapters(self,url):
        html=self.getSourceCode(url)
        selector=etree.HTML(html)
        print html
        print selector.xpath('//ul[@id="topic1"]/li/a/@title')[0]
        return selector.xpath('//ul[@id="topic1"]')



manhua163=defaultSpider('https://163.bilibili.com/')
shenmanhua=shenmanhuaSpider('https://www.shenmanhua.com')
# shenmanhua.getChapters('https://www.shenmanhua.com/shenyidinv/')
# print manhua163.getRecommend()