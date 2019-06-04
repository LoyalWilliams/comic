#coding=utf-8
import json
import re

import requests
from lxml import etree
from comicspider.spiders.defaultSpider import DefaultSpider


class Manhua163Spider(DefaultSpider):
    baseUrl = 'https://www.shenmanhua.com/'

    def getSourceCode(self,url):
        headers = self.headers
        response = requests.get(url, headers=headers, verify=False).content
        return response

    def getChapters(self,url):
        headers = self.headers
        sourceCode=self.getSourceCode(url)
        selector=etree.HTML(sourceCode)
        comicName = selector.xpath("//div[contains(@class,'header')]//h1/text()")[0]
        bookId = url[url.rindex('/')+1:]
        url='https://manhua.163.com/book/catalog/'+bookId
        response=requests.get(url,headers=headers,verify=False).content
        sections=json.loads(response)['catalog']['sections'][0]['sections']
        chapters=[]
        for each in sections:
            sectionId=each['sectionId']
            title=each['fullTitle']
            chapterUrl='https://manhua.163.com/reader/'+bookId+"/"+sectionId
            content={'comicName':comicName,'sectionId':sectionId,'title':title,'chapterUrl':chapterUrl}
            chapters.append(content)
        return chapters

    def getImgRealPath(self,url):
        headers = self.headers
        response = requests.get(url, headers=headers, verify=False).content
        pattern = re.compile(r'url: window.IS_SUPPORT_WEBP [?](.*)')
        imgUrls = pattern.findall(response)
        l=[]
        for each in imgUrls:
            imgUrl=each.replace('\"', '').rstrip(',').strip()
            imgUrl=imgUrl.split(' : ')
            pattern = re.compile(r'NOSAccessKeyId=(.*)')
            imgUrl=[re.sub(pattern, 'NOSAccessKeyId=c2e341292e09405fbdb6e6d41f77d91d', a).replace(' ','') for a in imgUrl]
            # print re.sub(pattern, 'NOSAccessKeyId=c2e341292e09405fbdb6e6d41f77d91d', imgUrl)
            l.append(imgUrl)
        return l

    def getInfoUrlByChapterUrl(self,chapterUrl):
        rindex1=chapterUrl.rindex('/')
        url=chapterUrl[0:rindex1]
        key=url[url.rindex('/')+1:]
        return 'https://manhua.163.com/source/'+key

    def getRecommend(self):
        recommendsText = self.getSourceCode('https://h5.manhua.163.com/reader/recommend/layer.json')
        recommends=json.loads(recommendsText)['recommends']
        recommends[0]['url']='https://manhua.163.com/source/'+recommends[0]['targetId']
        for recommend in recommends:
            recommend['url'] = 'https://manhua.163.com/source/' + recommend['targetId']
        return recommends

manhua163=Manhua163Spider()
