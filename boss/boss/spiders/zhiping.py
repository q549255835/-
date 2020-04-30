    # -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem


class ZhipingSpider(CrawlSpider):
    name = 'zhiping'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=python%E7%88%AC%E8%99%AB&page=1&ka=page-1']

    rules = (
        # 匹配列表页的规则
        Rule(LinkExtractor(allow=r'.+\?query=python%E7%88%AC%E8%99%AB&page=0'), follow=True),
        # 匹配职位详情页的规则
        Rule(LinkExtractor(allow=r'.+job_detail/(.*?).html'), callback='parse_job', follow=False),
    )

    def parse_job(self,response):
        title = response.xpath('//div[@class="name"]/h1/text()').extract()
        print('哈哈哈')
        print(title)