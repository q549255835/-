# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItems
from scrapy.linkextractors import LinkExtractor


class A88ysSpider(scrapy.Spider):
    name = '88ys'
    allowed_domains = ['88ys.com']
    start_urls = ['https://www.88ys.com/vod-type-id-1-pg-1.html']
    # 根据规则提取所有的页码链接
    page_link = LinkExtractor(restrict_xpaths='//div[@class="page mb clearfix"]/a')
    # follow: 是否跟进
    rules = (Rule(page_link, callback='parse_item', follow=False))

    url = 'https://www.88ys.com/vod-type-id-1-pg-1.html'
    page = 1

    def parse(self, response):
        #首先找到所有div
        div_list = response.xpath('//div[@class="index-area clearfix"]/ul/li')
        for odiv in div_list:
            item = MovieItems()
            item['post'] = odiv.xpath('.//img/@data-original').extract_first()
            item['name'] = odiv.xpath('.//img/@alt').extract_first()
            item['actor'] = odiv.xpath('.//a/span[2]/p[2]/text()').extract_first()
            item['leixing'] = odiv.xpath('/a/span[2]/p[3]/text()').extract_first()
            item['year_diqu'] = odiv.xpath('/a/span[2]/p[4]/text()').extract_first()
            # 获取详情页面链接
            detail_url = odiv.xpath('.//a/@href').extract_first()
            # 向详情页发送请求, 并且通过meta将item传递过去
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        # 通过response的meta属性获取到参数meta.
        item = response.meta['item']
        item['jianjie'] = response.xpath('//div[@name="ee"]').xpath('string(.)').extract_first()

