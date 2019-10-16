# -*- coding: utf-8 -*-
import scrapy
import urllib
from .default import DefaultComicSpider

class ShenmanhuaSpider(DefaultComicSpider):
    name = 'shenmanhua'
    allowed_domains = ['www.shenmanhua.com']
    url = 'https://www.shenmanhua.com/all_p'
    offset = 1
    start_urls = [url + str(offset)+'.html']


    def parse(self, response):
        hrefs = response.xpath("//a[contains(@class,'sdiv')]/@href").extract()
        for href in hrefs:
            yield scrapy.Request(urllib.basejoin('https://www.shenmanhua.com/',href), callback=self.detail_parse)

        if self.offset < 55:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset)+'.html', callback=self.parse)
        yield scrapy.Request('https://www.shenmanhua.com/doupocangqiong/', callback=self.detail_parse)

    def detail_parse(self, response):
        item=self.parse_item(response)
        # print item
        item['name']=item['name'].replace(u'名称：','').strip()
        item['author']=item['author'].replace(u'作者：','').strip()
        comic_type=item['comic_type'].replace(u'类型：','').strip().split(' ')
        item['comic_type']="|".join(comic_type).strip()
        item['comic_type2']=''
        item['collection'] =0
        item['recommend'] =0
        item['praise'] =0
        item['roast'] =0
        item['last_update_chapter'] = response.xpath("//div[contains(@class,'jshtml')]//li[2]/a/text()").extract()[0].strip()
        item['last_update_time'] = item['last_update_time'].replace(u'更新：','').strip()
        yield item
