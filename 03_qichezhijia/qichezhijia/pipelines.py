# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from qichezhijia import settings
    

class QichezhijiaPipeline(object):
    
    def __init__(self):

        #构建self.path的绝对路径
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')

        if not os.path.exists(self.path):
            
            os.mkdir(self.path)
        else:
            pass
    def process_item(self, item, spider):
        category = item['category']
        urls = item['urls']

        #构建category_path的绝对路径
        category_path = os.path.join(self.path, category)
        #判断文件是否存在
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for url in urls:
            image_name = url.split('_')[-1]
            request.urlretrieve(url,os.path.join(category_path, image_name))
        return item

# 想要像一开始用模块进行分组路径，重写file_path方法
class QichezhijiaImagesPipeline(ImagesPipeline):
    # 需要用到category但是这个类中没有 itme对像，需要把item传进来，重写这个方法 
    # 这个方法是在请求之前调用   
    def get_media_requests(self, item, info):
        #这个方法是在发送下载请求之前调用。
        # 其实这个方法本身就是去发送下载请求的
        print('我过来啦')
        request_objs = super(QichezhijiaImagesPipeline, self).get_media_requests(item, info)
        print('发送请求')
        print(request_objs)
        for request_obj in request_objs:
            #把item绑定到request_obj对象上去
            request_obj.item = item
        return request_objs
        
    # 重写file_path方法获得，分组创建文件夹的路径 
    def file_path(self, request, response=None, info=None):
        # 这个方法是在图片将要存储的时候调用，来获取这个图片的路径
        path = super(QichezhijiaImagesPipeline, self).file_path(request, response, info)

        category = request.item.get('category')
        images_store = settings.IMAGES_STORE
        category_path = os.path.join(images_store, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        image_name = path.replace("full/", "")
        image_path = os.path.join(category_path,image_name)
        return image_path













