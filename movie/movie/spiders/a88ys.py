# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem
from scrapy.linkextractors import LinkExtractor


class A88ysSpider(scrapy.Spider):
    name = '88ys'
    allowed_domains = ['88ys.com']
    start_urls = ['https://www.88ys.com/vod-type-id-1-pg-1.html']

    url = 'https://www.88ys.com/vod-type-id-1-pg-{}.html'
    page = 1

    def parse(self, response):
        #首先找到所有div
        div_list = response.xpath('//div[@class="index-area clearfix"]/ul/li')
        for odiv in div_list:
            item = MovieItem()
            item['post'] = odiv.xpath('.//img/@data-original').extract_first()
            item['name'] = odiv.xpath('.//img/@alt').extract_first()
            item['actor'] = odiv.xpath('.//a/span[2]/p[2]/text()').extract_first()
            item['leixing'] = odiv.xpath('/a/span[2]/p[3]/text()').extract_first()
            item['year_diqu'] = odiv.xpath('/a/span[2]/p[4]/text()').extract_first()
            # 获取详情页面链接
            detail_url = odiv.xpath('.//a/@href').extract_first()
            href_url = 'https://www.88ys.com' + detail_url
            # 向详情页发送请求, 并且通过meta将item传递过去
            yield scrapy.Request(url=href_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        # 通过response的meta属性获取到参数meta.
        item = response.meta['item']
        item['jianjie'] = response.xpath('//div[@name="ee"]').xpath('string(.)').extract_first()

        yield item

        if self.page <= 3:
            self.page += 1
            url = self.url.format(self.page)
            # 并向拼接成功url发送请求
            yield scrapy.Request(url, callback=self.parse)


