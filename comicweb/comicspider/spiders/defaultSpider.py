#coding=utf-8
import json
import re
import urllib
from bs4 import BeautifulSoup
import requests

from comicspider import settings


class DefaultSpider():
    baseUrl='https://www.xxx.com'
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
            }
        self.rule= settings.getRule(self.baseUrl)

    def getSourceCode(self,url):
        headers = self.headers
        response = requests.get(url, headers=headers, verify=False).content
        return response

    def getChapters(self, url):
        html = self.getSourceCode(url)
        selector = BeautifulSoup(html, 'lxml')
        chaptersA = selector.select(self.rule.get('chapter-selector'))
        chapters = []
        for each in chaptersA:
            title = each.string.strip()
            chapterUrl = each['href']
            chapterUrl = urllib.basejoin(self.baseUrl, chapterUrl)
            content = {'title': title, 'chapterUrl': chapterUrl}
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
            imgUrl=[re.sub(pattern, 'NOSAccessKeyId=c92f74b0d48f4fb39271a1109da74cc2', a).replace(' ','') for a in imgUrl]
            # print re.sub(pattern, 'NOSAccessKeyId=c92f74b0d48f4fb39271a1109da74cc2', imgUrl)
            l.append(imgUrl)
        return l


    def getRecommend(self):
        recommendsText = self.getSourceCode('https://h5.manhua.163.com/reader/recommend/layer.json')
        recommends=json.loads(recommendsText)['recommends']
        recommends[0]['url']='https://manhua.163.com/source/'+recommends[0]['targetId']
        for recommend in recommends:
            recommend['url'] = 'https://manhua.163.com/source/' + recommend['targetId']
        return recommends
