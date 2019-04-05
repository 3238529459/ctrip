# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def process_request(self,request,spider):
        self.driver.get(request.url)
        time.sleep(1)
        source = self.driver.page_source
        response = HtmlResponse(url=self.driver.current_url,body=source,
                                request=request,encoding='utf-8')
        return response