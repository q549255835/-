# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter

class FangPipeline(object):
    def __init__(self):
        self.newhouse_fp = open('newhouse.josn', 'wb')
        self.rsfhouse_fp = open('rsfhouse.josn', 'wb')
        self.newhouse_exporter = JsonLinesItemExporter(self.newhouse_fp,ensure_ascii=False)
        self.rsfhouse_exporter = JsonLinesItemExporter(self.rsfhouse_fp,ensure_ascii=False)

    def process_item(self, item, spider):
        self.newhouse_exporter.export_item(item)
        self.rsfhouse_exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.newhouse_fp.close()
        self.rsfhouse_fp.close()
