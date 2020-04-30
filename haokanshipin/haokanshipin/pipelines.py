# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request

class HaokanshipinPipeline(object):
    def __init__(self):
        #构建self.path的绝对路径 在本文件的上一级的上一级下创建
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'video')
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        else:
            pass  

    def process_item(self, item, spider):
        name = item['name']

        video_url = item['video_url']

        video_name = name
        request.urlretrieve(video_url, os.path.join(self.path, video_name))
    
        return item


