# -*- coding: utf-8 -*-
import scrapy
import json
from comicscrapy.items import ComicscrapyItem
import time

class Manhua163Spider(scrapy.Spider):
    name = 'manhua163'
    allowed_domains = ['manhua.163.com']
    url='https://manhua.163.com/category/getData.json?sort=2&sf=1&pageSize=72&page='
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
            a = time.localtime(int(book['latestPublishTime'])/1000);  ##获取昨天日期
            timestr = time.strftime("%Y-%m-%d %H:%M:%S", a)
            item['last_update_time'] = timestr
            item['comic_url'] = 'https://manhua.163.com/source/'+book['bookId']
            yield scrapy.Request(url=item['comic_url'],meta={'item':item},callback=self.detail_parse)

        if self.offset < 71:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def detail_parse(self, response):
        item=response.meta['item']
        comic_type=response.xpath("//dl[contains(@class,'sr-dl')]/dd[2]/a/text()").extract()
        item['comic_type']="|".join(comic_type).strip()
        item['comic_type2']=''
        item['collection']=0
        item['recommend']=0
        praise = response.xpath("//dl[contains(@class,'sr-dl')]/dd[3]/span/text()").extract()[0]
        item['praise']=self.paseNum(praise)
        roast = response.xpath("//dl[contains(@class,'sr-dl')]/dd[4]/span/text()").extract()[0]
        item['roast']=self.paseNum(roast)
        status = response.xpath("//dl[contains(@class,'sr-dl')]/dd[1]/a[1]/text()").extract()[0]
        if u'连载' in status :
            item['status']=1
        else:
            item['status'] = 0
        # print dict(item)

        yield item

    def paseNum(self,str):
        if u'万' in str:
            num=float(str.replace(u'万', ''))
            return int(num*10000)
        elif u'亿' in str:
            num = float(str.replace(u'亿', ''))
            return int(num * 100000000)
        else:
            return int(str)



