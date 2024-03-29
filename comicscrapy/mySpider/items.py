# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    comic_id              =scrapy.Field()
    chapter_id            =scrapy.Field()
    name                  =scrapy.Field()
    last_short_title      =scrapy.Field()
    author                =scrapy.Field()
    cover                 =scrapy.Field()
    intr                  =scrapy.Field()
    chapter_title         =scrapy.Field()
    chapter_short_title   =scrapy.Field()
    chapter_time          =scrapy.Field()
    urls                  =scrapy.Field()
    add_time              =scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    paths = scrapy.Field()

