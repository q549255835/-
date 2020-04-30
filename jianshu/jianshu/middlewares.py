# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from time 
from scrapy.http.response.html import HtmlResponse

class SeleniumDownloadMiddleware(objiect):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"/Applications/chromedriver")
    
    def process_request(self,requset,spider):
        self.driver.get(requset.url)
        time.sleep(1)
        try:
            while True:
                showMore = self.driver.find_element_by_class_name('show-more')
                showMore.click()
                time.sleep(0.3)
                if not showMore:
                    break
        except:
            pass
            
        source = self.driver.page_source
        response = HtmlResponse(url=self.driver.current_url,body=source,requset=requset)
        return response
