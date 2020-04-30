# -*- coding: utf-8 -*-
import scrapy
from haokanshipin.items import HaokanshipinItem
import json
import urllib.request
import urllib.parse
import jsonpath
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class HaokanSpider(scrapy.Spider):
    name = 'haokan'
    #allowed_domains = ['https://haokan.baidu.com/']

     
    def start_requests(self):
        furl = 'https://haokan.baidu.com/videoui/api/videorec?tab=gaoxiao&act=pcFeed&pd=pc&num=20&shuaxin_id=1586100322492'
        for i in range(1, 2):

            yield scrapy.Request(url=furl, callback=self.parse_list, dont_filter = True)
        
    def parse_list(self, response):
        #返回json格式，转为python字典
        js_list = json.loads(response.text)
        #with open('json.html', 'w', encoding='utf8') as fp:
        #    fp.write(str(js_list))
        #print(js_list)
        #print(str(js_list))
        #video_list = jsonpath.jsonpath(js_list, '$..Object')
        data = js_list['data']
        response = data['response']
        videos = response['videos']
        for video in videos:
            item = HaokanshipinItem()
            item['post'] = video['poster']
            item['name'] = video['title']
            print(item['name'])
            item['bofang'] = video['fmplaycnt']
            item['comment'] = video['comment']
            item['video_url'] = video['play_url']
            
            print('哇哈哈哈哈哈哈')
            
            yield item
            print('嘿嘿嘿嘿嘿')


        """
        本项目存在视频url访问如何下载问题及如何保存到本地文件
        问题解决：
        在pipelines 文件中直接创建链接访问！















 

