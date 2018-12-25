# -*- coding: utf-8 -*-
import scrapy
import urllib
from comicscrapy.items import ComicscrapyItem
import time
from comicscrapy import rules
import sys

class DefaultComicSpider(scrapy.Spider):
    name = ''
    allowed_domains = ['']
    url = ''
    offset = 1
    start_urls = []
    ITEM_PIPELINES = {
        'comicscrapy.pipelines.ComicscrapyPipeline': 300,
    }
    custom_settings={
        'ITEM_PIPELINES':ITEM_PIPELINES
    }

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.spider_rule = rules.getRule(self.allowed_domains[0])
        print self.spider_rule

    def parse(self, response):
        hrefs = response.xpath("//a[contains(@class,'sdiv')]/@href").extract()
        for href in hrefs:
            yield scrapy.Request(urllib.basejoin('https://www.shenmanhua.com/',href), callback=self.detail_parse)

        if self.offset < 55:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset)+'.html', callback=self.parse)
        yield scrapy.Request('https://www.shenmanhua.com/doupocangqiong/', callback=self.detail_parse)

    def detail_parse(self, response):
        item = self.parse_item(response)
        yield item


    def parse_item(self, response):
        spider_rule=self.spider_rule
        rule_keys=spider_rule.keys()
        item = ComicscrapyItem()
        item['comic_url'] = response.url
        # move = dict.fromkeys((ord(c) for c in u"\xa0"))
        move = {160: 32}
        if 'author-selector' in rule_keys:
            item['author'] = response.xpath(spider_rule['author-selector']).extract()[0].strip().translate(move)
        if 'name-selector' in rule_keys:
            item['name'] = response.xpath(spider_rule['name-selector']).extract()[0].strip().translate(move)
        if 'intr-selector' in rule_keys:
            item['intr'] = response.xpath(spider_rule['intr-selector']).extract()[0].strip().translate(move)
        if 'cover-selector' in rule_keys:
            item['cover'] = response.xpath(spider_rule['cover-selector']).extract()[0].strip().translate(move)
        if 'comic_url-selector' in rule_keys:
            item['comic_url'] = response.xpath(spider_rule['comic_url-selector']).extract()[0].strip().translate(move)
        if 'comic_type-selector' in rule_keys:
            comic_type = response.xpath(spider_rule['comic_type-selector']).extract()
            item['comic_type'] = '|'.join(comic_type).strip()
        if 'comic_type2-selector' in rule_keys:
            item['comic_type2'] = response.xpath(spider_rule['comic_type2-selector']).extract()[0].strip().translate(move)
        else:
            item['comic_type2'] = ''
        if 'collection-selector' in rule_keys:
            collection = response.xpath(spider_rule['collection-selector']).extract()[0].strip().translate(move)
            item['collection'] = self.paseNum(collection)
        else:
            item['collection'] = 0
        if 'recommend-selector' in rule_keys:
            recommend = response.xpath(spider_rule['recommend-selector']).extract()[0].strip().translate(move)
            item['recommend'] = self.paseNum(recommend)
        else:
            item['recommend'] = 0
        if 'praise-selector' in rule_keys:
            item['praise'] = response.xpath(spider_rule['praise-selector']).extract()[0].strip().translate(move)
            praise = response.xpath(spider_rule['praise-selector']).extract()[0].strip().translate(move)
            item['praise'] = self.paseNum(praise)
        else:
            item['praise'] = 0
        if 'roast-selector' in rule_keys:
            roast = response.xpath(spider_rule['roast-selector']).extract()[0].strip().translate(move)
            item['roast'] = self.paseNum(roast)
        else:
            item['roast'] = 0

        if 'last_update_chapter-selector' in rule_keys:
            item['last_update_chapter'] = \
                response.xpath(spider_rule['last_update_chapter-selector']).extract()[0].strip().translate(move)
        if 'last_update_time-selector' in rule_keys:
            item['last_update_time'] = response.xpath(spider_rule['last_update_time-selector']).extract()[0].strip().translate(move)
        if 'status-selector' in rule_keys:
            status = response.xpath(spider_rule['status-selector']).extract()[0].strip().translate(move)
            if u'连载' in status:
                item['status'] = 1
            else:
                item['status'] = 0
        return item

    def paseNum(self,str):
        str = str.replace(',', '')
        if u'万' in str:
            num=float(str.replace(u'万', ''))
            return int(num*10000)
        elif u'亿' in str:
            num = float(str.replace(u'亿', ''))
            return int(num * 100000000)
        else:
            return int(str)

