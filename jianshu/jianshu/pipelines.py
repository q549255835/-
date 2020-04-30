# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# 数据库处理的模块
from twisted.enterprise import adbapi

# 数据存入mysql数据库
class JianshuPipeline(object):
    def __init__(self):
        dbparams = {
            'host': ,
            'port': ,
            'user': ,
            'password': ,
            'database': ,
            'charset': 'utf8'
        }
        self.conn = pymysql,connect(**dbparams)
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
    	self.cursor.execute(self.sql,(item['title'],item['content']))



    @property
    def sql(self):
        if not self._sql:
        	self._sql = """
        	insert ino article(id,title,content,author,acatar,pub_time,origin_url,article_id) calues(null,%s,%s,%s,%s,%s,%s,%s)
        	"""
        	return self._sql
        return self._sql



class JianshuTwistedPipeline(object):
	def __init__(self):
		self.dbpool = adbapi.ConnectionPool('pymysql')
		# 数据库连接信息参数








    