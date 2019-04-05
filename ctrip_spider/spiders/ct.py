# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ctrip_spider.items import CtripSpiderItem


class CtSpider(CrawlSpider):
    name = 'ct'
    allowed_domains = ['flights.ctrip.com']
    start_urls = ['https://flights.ctrip.com/itinerary/oneway/can-ctu?date=2019-04-04']

    rules = (
        Rule(LinkExtractor(allow=r'.+/itinerary/oneway/[a-zA-Z]{3}-[a-zA-Z]{3}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        ret = response.xpath("//div[@class='search_box search_box_tag search_box_light Label_Flight']")
        content_list = []
        url = response.url
        url1 = url.split("?")[0]
        url2 = url.split("?")[-1]
        url3 = url1.split("/")[-1]
        url4 = url3.split("-")[0]
        url5 = url3.split("-")[1]
        url6 = url2.split("&")[0]
        url7 = url6.split("=")[-1]
        for li in ret:
            item1 = {}
            item1["出发地点1"] = url4
            item1["到达地点1"] = url5
            item1["出发日期"] = url7
            item1["准点率"] = li.xpath(".//div[@class='clearfix']//text()").get()
            item1["航空公司"] = li.xpath(".//div[@class='logo-item flight_logo']//strong/text()").get()
            item1["飞机类型"] = li.xpath(".//div[@class='inb logo']//span/text()").get()
            item1["出发时间"] = li.xpath(".//div[@class='inb right']/div[@class='time_box']/strong/text()").get()
            item1["出发地点"] = li.xpath(".//div[@class='inb right']/div[@class='airport']/text()").get()
            item1["到达时间"] = li.xpath(".//div[@class='inb left']/div[@class='time_box']/strong/text()").get()
            item1["到达地点"] = li.xpath(".//div[@class='inb left']/div[@class='airport']/text()").get()
            item1["价格"] = li.xpath(
                "./div[@class='search_table_header']//span[@class='base_price02']/text()").get()
            content_list.append(item1)
        for it in content_list:
            start_place = it["出发地点1"]
            arrive_place = it["到达地点1"]
            date = it["出发日期"]
            airplane_company = it["航空公司"]
            airplane = it["飞机类型"]
            arrive_correct = it["准点率"]
            price = it["价格"]
            start_time = it["出发时间"]
            arrive_time = it["到达时间"]
            start_airport = it["出发地点"]
            arrive_airport = it["到达地点"]
            item = CtripSpiderItem(start_place=start_place,arrive_place=arrive_place,date=date,
                                   airplane_company=airplane_company,airplane=airplane,
                                   arrive_correct=arrive_correct,price=price,start_time=start_time,
                                   arrive_time=arrive_time,start_airport=start_airport,arrive_airport=arrive_airport)
            yield item
