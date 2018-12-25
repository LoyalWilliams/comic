# -*- coding: utf-8 -*-
import scrapy
import urllib
from comicscrapy.spiders.default import DefaultComicSpider
import json

class TencentmanhuaSpider(DefaultComicSpider):
    name = 'tencentmanhua'
    allowed_domains = ['ac.qq.com']
    url = 'https://ac.qq.com/Comic/all/search/time/vip/1/page/'
    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response):
        hrefs = response.xpath("//div[contains(@class,'ret-works-cover')]/a/@href").extract()
        for href in hrefs:
            yield scrapy.Request(urllib.basejoin('https://ac.qq.com/', href), callback=self.detail_parse)
        # yield scrapy.Request('https://ac.qq.com/Comic/comicInfo/id/636578', callback=self.detail_parse)

        if self.offset < 793:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def detail_parse(self,response):
        item = self.parse_item(response)
        url = response.url
        item['author']=item['author'].split(' ')[0]
        item['last_update_chapter']=item['last_update_chapter'].lstrip('[').rstrip(']')
        last_update_time=''.join(item['last_update_time'].split('.'))
        item['last_update_time']=last_update_time[0:8]
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Referer': url
        }
        comicId=url[url.rindex('/')+1:]
        yield scrapy.Request('https://ac.qq.com/Comic/userComicInfo?comicId='+comicId, headers=headers, callback=self.getComicType,meta={'item':item})
        # print item

    def getComicType(self,response):
        item = response.meta['item']
        jtext = response.text
        tag = json.loads(jtext)['tag']
        comic_type=''
        for t in tag:
            comic_type = comic_type+'|'+t['name']
        item['comic_type']=comic_type[1:]
        yield item

