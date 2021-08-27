# -*- coding: utf-8 -*-
import scrapy
import json
from mySpider.items import MyspiderItem
import copy

class Manhua163Spider(scrapy.Spider):
    name = 'bilibili'
    headers = {'Content-Type': 'application/json',
               'user-agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'}
    allowed_domains = ['163.bilibili.com', 'manga.bilibili.com']
    url = 'https://manga.bilibili.com/'
    start_urls = [url]

    def parse(self, response):
        # 一共56页
        target_url = 'https://manga.bilibili.com/twirp/comic.v1.Comic/ClassPage?device=pc&platform=web'
        for i in range(1, 57):
            data = {
                "style_id": -1,
                "area_id": -1,
                "is_finish": -1,
                "order": 0,
                "page_num": i,
                "page_size": 18,
                "is_free": 1
            }
            # scrapy.FormRequest(target_url, formdata=json.dumps(data), callback=self.parse_comic)
            yield scrapy.Request(target_url, body=json.dumps(data), method='POST',  callback=self.parse_comic, headers=self.headers)

    def parse_comic(self, response):
        jtext = response.text
        data = json.loads(jtext)
        for comic in data['data']:
            comic_id = comic['season_id']
            # comic_id = 25501
            form_data = {
                "comic_id": comic_id
            }
            target_url = 'https://manga.bilibili.com/twirp/comic.v1.Comic/ComicDetail?device=pc&platform=web'
            yield scrapy.Request(target_url,
                                 body=json.dumps(form_data), method='POST', callback=self.detail_parse,
                                 headers=self.headers)

    def detail_parse(self, response):
        jtext = response.text
        data = json.loads(jtext)
        ep_list = data['data']['ep_list']
        item = MyspiderItem()
        item['comic_id'] = data['data']['id']
        item['name'] = data['data']['title']
        item['author'] = data['data']['author_name']
        item['cover'] = data['data']['vertical_cover']
        item['intr'] = data['data']['evaluate']
        item['last_short_title'] = data['data']['last_short_title']
        for ep in ep_list:
            form_data = {"ep_id": ep['id']}
            item = copy.deepcopy(item)
            item['chapter_title'] = ep['title']
            item['chapter_id'] = ep['id']
            item['chapter_short_title'] = ep['short_title']
            item['chapter_time'] = ep['pub_time']
            target_url = 'https://manga.bilibili.com/twirp/comic.v1.Comic/GetImageIndex?device=pc&platform=web'
            # self.log(item)
            # self.log('qqqqqqqqqq')
            yield scrapy.Request(target_url,
                                 body=json.dumps(form_data), method='POST',
                                 callback=self.comic_info, meta={'item': item}, headers=self.headers)

    def comic_info(self, response):
        jtext = response.text
        item = response.meta['item']
        data = json.loads(jtext)
        images = data['data']['images']
        urls = [image['path']+"@1100w.jpg" for image in images]
        form_data = {
            "urls": json.dumps(urls)
        }
        target_url = 'https://manga.bilibili.com/twirp/comic.v1.Comic/ImageToken?device=pc&platform=web'
        yield scrapy.Request(target_url,
                             body=json.dumps(form_data), method='POST',
                             callback=self.get_imgs, meta={'item': item},
                             headers=self.headers)

    def get_imgs(self, response):
        jtext = response.text
        item = response.meta['item']
        data = json.loads(jtext)
        item['image_urls'] = [url_token['url']+'?token='+url_token['token']
                              for url_token in data['data']]
        item['urls'] = json.dumps(
            [url_token['url']+'?token='+url_token['token'] for url_token in data['data']])
        yield item
