# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
class MoviePipeline(object):
    # 重写这个方法，当爬虫开启的时候会调用这个
    def open_spider(self, spider):
        self.fp = open('movie.mp4', 'w', encoding='utf8') 
    def process_item(self, item, spider):
        # 要将item保存到文件中
        # 将对象转化为字典
        dic = dict(item)
        # 将字典转化为json格式
        string = json.dumps(dic, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item
        

    # 当爬虫结束的调用这个方法
    def close_spider(self, spider):
        self.fp.close()
