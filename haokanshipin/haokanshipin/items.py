# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HaokanshipinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    post = scrapy.Field()
    name = scrapy.Field()
    bofang = scrapy.Field()
    comment = scrapy.Field()
    video_url = scrapy.Field()