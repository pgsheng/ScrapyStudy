"""
 @Author  : pgsheng
 @Time    : 2018/10/30 15:09
"""
import time

import scrapy

from ScrapyStudy.items import Sina7x24Item, BeautyImageItem
from ScrapyStudy.public import Config
from ScrapyStudy.public.Log import Log


class BeautyImageSpider(scrapy.Spider):
    name = "BeautyImageSpider"
    allowed_domains = ["lab.scrapyd.cn"]
    start_urls = [
        'http://lab.scrapyd.cn/archives/55.html'
    ]
    custom_settings = {
        # 'ITEM_PIPELINES': {'ScrapyStudy.pipelines.Sina7x24Pipeline': 300, },
        # 'DOWNLOADER_MIDDLEWARES': {"ScrapyStudy.middlewares.SeleniumMiddleware": 401, },
    }

    def __init__(self):
        self.log = Log().get_logger()
        super(BeautyImageSpider, self).__init__()

    def start_requests(self):
        for urls in self.start_urls:
            yield scrapy.Request(url=urls, callback=self.parse)

    def parse(self, response):
        # filename = Config.get_results_path() + "beauty_image.html"  # 1、保存网页数据
        # with open(filename, 'wb+') as file:  # 只能以二进制方式打开
        #     file.write(response.body)

        items = []
        item = BeautyImageItem()

        return items  # 直接返回最后数据

    def closed(self, spider):
        self.log.info("BeautyImageSpider_closed")
