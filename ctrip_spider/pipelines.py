# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class CtripSpiderPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'ctrip',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['start_place'], item['arrive_place'],
                                       item['date'], item['airplane_company'], item['airplane'],
                                       item['arrive_correct'], item['price'], item['start_time'],
                                       item['arrive_time'], item['start_airport'], item['arrive_airport']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into airport(id,start_place,
            arrive_place,date,airplane_company,airplane,arrive_correct,price,
            start_time,arrive_time,start_airport,arrive_airport) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
        return self._sql
