# -*- coding: utf-8 -*-
import scrapy
from qichezhijia.items import QichezhijiaItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule

# https://car2.autoimg.cn/cardfs/product/g1/M02/1E/82/240x180_0_q95_c42_autohomecar__ChsEmV28d1GAPIUQAAbFMmgQa4I527.jpg

# https://car2.autoimg.cn/cardfs/product/g1/M02/1E/82/1024x0_1_q95_autohomecar__ChsEmV28d1GAPIUQAAbFMmgQa4I527.jpg

# https://car.autohome.com.cn/pic/series/202-1.html#pvareaid=2042222
# https://car.autohome.com.cn/pic/series/202-10.html#pvareaid=2042222
# https://car.autohome.com.cn/pic/series/202-3.html#pvareaid=2042222
# https://car.autohome.com.cn/pic/series/202-10-p2.html

#https://car3.autoimg.cn/cardfs/product/g29/M0A/00/26/240x180_0_q95_c42_autohomecar__ChsEfl28doSATmViAAcGHbozzXw825.jpg

#https://car3.autoimg.cn/cardfs/product/g29/M0A/00/26/1024x0_1_q95_autohomecar__ChsEfl28doSATmViAAcGHbozzXw825.jpg



class QczjSpider(scrapy.Spider):
    name = 'qczj'
    allowed_domains = ['https://www.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/202.html#pvareaid=3454438']

    rules = (Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/202.+'), callback='parse', follow=True))
    print('hahahahaha')
    def parse(self, response):
        category = response.xpath('//div[@class="uibox"]/div[2]/ul/li/a/@title').extract()
        image_urls = response.xpath('//div[@class="uibox"]/div[2]/ul/li/a/img/@src').extract()
        #print(image_urls)
        #print('哈哈哈哈哈')
        for image in image_urls:
            #print('嘿嘿嘿')
            image = 'https:' + image.replace('240x180_0_q95_c42', '1024x0_1_q95')
            print(image)

            yield QichezhijiaItem(category=category, image_urls=image)
            print('封装完成')





"""
def text_parse(sefl,response):
        uibox_list = response.xpath('//div[@class="uibox"]')[1:]
        for uibox in uibox_list:
            category = uibox.xpath('.//div[2]/ul/li/a/@title').extract_first()
            urls = uibox.xpath('.//div[2]/ul/li/a/img/@src').getall()
            
            获取图片拼接链接：方法二
            urls = uibox.xpath('.//div[2]/ul/li/a/img/@src').getall()
            url = 'https:' + urls
            print(url)

            获取图片拼接链接：方法二
            for url in urls:
                url = response.urljoin(url)  # url = 'https' + url
                print(url)
            

            # 使用 map函数
            urls = list(map(lambda url:response.urljoin(url),urls))
            item = QichezhijiaItem(category=category, image_urls=urls)
            yield item
            
""" 
             















