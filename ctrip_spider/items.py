# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CtripSpiderItem(scrapy.Item):
    start_place = scrapy.Field()
    arrive_place = scrapy.Field()
    date = scrapy.Field()
    airplane_company = scrapy.Field()
    airplane = scrapy.Field()
    arrive_correct = scrapy.Field()
    price = scrapy.Field()
    start_time = scrapy.Field()
    arrive_time = scrapy.Field()
    start_airport = scrapy.Field()
    arrive_airport = scrapy.Field()