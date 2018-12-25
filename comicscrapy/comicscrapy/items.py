# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ComicscrapyItem(scrapy.Item):
    author = scrapy.Field()
    name = scrapy.Field()
    intr = scrapy.Field()
    cover = scrapy.Field()
    comic_url = scrapy.Field()
    comic_type = scrapy.Field()
    comic_type2 = scrapy.Field()
    collection = scrapy.Field()
    recommend = scrapy.Field()
    praise = scrapy.Field()
    roast = scrapy.Field()
    last_update_chapter = scrapy.Field()
    last_update_time = scrapy.Field()
    status = scrapy.Field()
    add_time = scrapy.Field()


