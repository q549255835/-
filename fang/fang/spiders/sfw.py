# -*- coding: utf-8 -*-
import scrapy
import re
from fang.items import NewhouseItem,RSFHouseItem
class SfwSpider(scrapy.Spider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        # 获取全国省份对应城市名及城市链接
        trs = response.xpath('//div[@class="outCont"]//tr')
        province = None
        for tr in trs:
            tds = tr.xpath('.//td[not(@class)]')
            province_td = tds[0]
            province_text = province_td.xpath('.//text()').get()
            province_text = re.sub(r"\s","",province_text)
            if province_text:
                province = province_text
            city_td = tds[1]
            city_links = city_td.xpath('.//a')
            #print(city_links)
            for city_link in city_links:
                city = city_link.xpath('.//text()').get()
                city_url = city_link.xpath('.//@href').get()
                #print('省份',province)
                #print('城市链接',city_url)
                

                # 构建新房的url链接
                url_module = city_url.replace('.fang','.newhouse.fang')
                #print("这里是拼接链接",url_module)
                
                newhouse = url_module + 'house/s/'
                #print(newhouse)

                # 构建二手房的url链接
                rsf_url = city_url.replace('.fang','.esf.fang')
                #print('城市:%s%s'%(province,city))
                #print('新房链接: %s' %newhouse)
                print('二手房链接: %s' %rsf_url)

                #yield scrapy.Request(url=newhouse,callback=self.parse_newhouse,meta={"info":(province,city)})
                yield scrapy.Request(url=rsf_url,callback=self.parse_rsf,meta={"info":(province,city)})

                break
            break

    def parse_newhouse(self,response):
        province,city = response.meta.get('info')
        lis = response.xpath('//div[@ctm-data="lplist"]/ul/li')
        for li in lis:           
            try:
                name = li.xpath('.//div/div[2]/div/div/a/text()').get().strip()
                rooms = li.xpath('.//div/div[2]/div[2]/a/text()').getall()
            except Exception as e:
                pass
            #print(name)
            #print(rooms)
            area = "".join(li.xpath('.//div/div[2]/div[2]/text()').getall()).replace(' ','').replace('－','').replace('\s','').replace('/','')
            area = area.strip()
            #print(area)
            address = li.xpath('.//div/div[2]/div[3]/div/a/@title').get()
            #print(address)
            district = li.xpath('.//div/div[2]/div[3]/div/a/span/text()').get()
            try:
                district = district.strip()

            except Exception as e:
                print('[]')

            #print(district)
            sale = li.xpath('.//div/div[2]/div[4]/span/text()').get()
            #print(sale)
            price = "".join(li.xpath('.//div/div[2]/div[5]//text()').getall()).strip()
            #print(price)
            origin_url = li.xpath('.//div/div[2]/div/div/a/@href').get()
            origin_url = 'https:' + str(origin_url)
            #print(origin_url)
            
            item = NewhouseItem(name=name, rooms=rooms,area=area,address=address,district=district,sale=sale,price=price,origin_url=origin_url,province=province,city=city)
            yield item
        
        # 遍历所有页码
        next_url = response.xpath('//div[@class="page"]/ul/li[2]')
        for url in next_url:        
            url = url.xpath('.//a/@href').get()
            # 拼接下一页
            next_url = response.urljoin(url)          
            print(next_url)

            if next_url:
                yield scrapy.Request(url=next_url,callback=self.parse_newhouse,meta={"info":(province,city)})



    def parse_rsf(self,response):
        province,city = response.meta.get('info')
        item = RSFHouseItem(province=province,city=city)
        dls = response.xpath('//dl[@class="clearfix"]')
        for dl in dls:
            try:
                item["name"] = dl.xpath('.//p[@class="add_shop"]/a/text()').extract().strip()
            except Exception as e:
                pass           
            #print("小区",name)
            infos = dl.xpath('.//p[@class="tel_shop"]/text()').getall()
            infos = list(map(lambda x:re.sub(r"\s","",x),infos))
            #print(infos)
            for info in infos:
                if "厅" in info:
                    item["rooms"] = info
                elif "层" in info:
                    item["floor"] = info
                elif "向" in info:
                    item["toward"] = info
                elif "㎡" in info:
                    item["area"] = info
                elif "年" in info:
                    item["year"] = info
                #print(item)
            item["address"] = dl.xpath('.//dd/p[2]/span/text()').get()           
            price = dl.xpath('.//dd[2]/span/b/text()').get()
            item["price"] = str(price) + "万"
            item["unit"] = dl.xpath('.//dd[2]/span[2]/text()').get()
            #print(unit)
            origin_url = dl.xpath('.//dd[1]/h4/a/@href').get()
            item["origin_url"] = response.urljoin(origin_url)
            #print(origin_url)
            yield item

        next_url = response.xpath('//p[1]/a/@href').get()
        yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse_rsf,meta={"info":(province,city)})







              




