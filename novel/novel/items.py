# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    """
    小说
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()

class ChapterItem(scrapy.Item):
    """
    章节
    """
    title = scrapy.Field()
    # 对应小说的id
    id = scrapy.Field()
    # 对应小说的name
    name = scrapy.Field()
    content = scrapy.Field()
