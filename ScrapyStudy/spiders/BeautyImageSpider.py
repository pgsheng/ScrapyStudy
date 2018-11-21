"""
 @Author  : pgsheng
 @Time    : 2018/10/30 15:09
"""

import scrapy

from ScrapyStudy.items import BeautyImageItem
from ScrapyStudy.public.Log import Log


class BeautyImageSpider(scrapy.Spider):
    name = "BeautyImageSpider"
    allowed_domains = ["lab.scrapyd.cn"]
    start_urls = [
        'http://lab.scrapyd.cn/archives/55.html'
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'ScrapyStudy.pipelines.BeautyImagePipeline': 300, },
        # 'DOWNLOADER_MIDDLEWARES': {"ScrapyStudy.middlewares.SeleniumMiddleware": 401, },
        'IMAGES_STORE': 'D:\ImageSpider',  # 图片存储位置
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

        item = BeautyImageItem()
        # image_urls = response.css(".post-content img::attr(src)").extract()  # 图片url集合
        image_urls = response.xpath('//div[@class="post-content"]//img/@src').extract()
        item['image_url'] = image_urls

        yield item  # 直接返回最后数据

    def closed(self, spider):
        self.log.info("BeautyImageSpider_closed")
