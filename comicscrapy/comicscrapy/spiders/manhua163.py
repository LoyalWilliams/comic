# -*- coding: utf-8 -*-
import scrapy
import json
from comicscrapy.items import ComicscrapyItem
import time
from comicscrapy.spiders.default import DefaultComicSpider


class Manhua163Spider(DefaultComicSpider):
    name = 'manhua163'
    allowed_domains = ['163.bilibili.com']
    url='https://163.bilibili.com/category/getData.json?sort=2&sf=1&pageSize=72&page='
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        jtext = response.text
        books = json.loads(jtext)['books']
        for book in books:
            item = ComicscrapyItem()
            item['cover'] = book['cover']
            item['author'] = book['author']
            item['name'] = book['title']
            item['intr'] = book['description']
            item['last_update_chapter'] = book['latestSectionFullTitle']
            a = time.localtime(int(book['latestPublishTime'])/1000)  ##获取昨天日期
            timestr = time.strftime("%Y-%m-%d %H:%M:%S", a)
            item['last_update_time'] = timestr
            item['comic_url'] = 'https://163.bilibili.com/source/'+book['bookId']
            yield scrapy.Request(url=item['comic_url'],meta={'item':item},callback=self.detail_parse)

        if self.offset < 71:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def detail_parse(self, response):
        item=response.meta['item']
        item0 = self.parse_item(response)
        item['comic_type']=item0['comic_type']
        item['comic_type2']=''
        item['collection']=0
        item['recommend']=0
        item['praise']=item0['praise']
        item['roast']=item0['roast']
        item['status']=item0['status']
        yield item




