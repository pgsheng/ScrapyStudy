"""
 @Author  : pgsheng
 @Time    : 2018/10/30 15:09
"""
import time

import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from ScrapyStudy.items import Sina7x24Item
from ScrapyStudy.public.Log import Log


class Sina7x24Spider(scrapy.Spider):
    name = "sina7x24"
    allowed_domains = ["finance.sina.com.cn"]
    # start_urls = [
    #     'http://finance.sina.com.cn/7x24/'
    # ]
    custom_settings = {
        'ITEM_PIPELINES': {'ScrapyStudy.pipelines.Sina7x24Pipeline': 300, },
        'DOWNLOADER_MIDDLEWARES': {"ScrapyStudy.middlewares.SeleniumMiddleware": 401, },
        'CONCURRENT_REQUESTS' : 1,
    }

    def __init__(self):
        self.log = Log().get_logger()
        options = Options()  # 不同浏览器导入Options包路径不一样
        options.add_argument('-headless')  # 无界面配置
        self.driver = webdriver.Firefox(firefox_options=options)  # 这里初始化浏览很耗时
        # self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        self.driver.set_page_load_timeout(25)
        self.date_list = []
        self.is_first = True
        super(Sina7x24Spider, self).__init__()

    def start_requests(self):
        urls = 'http://finance.sina.com.cn/7x24/'
        # while True:
        for i in range(50):
            time.sleep(10)
            yield scrapy.Request(url=urls, callback=self.parse, dont_filter=True)  # dont_filte为True,不去重

    def parse(self, response):
        # filename = Config.get_results_path() + "sina7x24.html"  # 1、保存网页数据
        # with open(filename, 'wb+') as file:  # 只能以二进制方式打开
        #     file.write(response.body)

        items = []
        news = response.xpath("//div[@class='bd_i bd_i_og  clearfix']")
        day = time.strftime("%Y-%m-%d ", time.localtime(time.time()))  # 获取当前时间
        for each in news[::-1]:
            item = Sina7x24Item()
            # extract()方法返回的都是unicode字符串,normalize-space()可以去掉数据中空格、换行符等特殊符号
            times = each.xpath("normalize-space(div/p/text())").extract()
            info = each.xpath("normalize-space(div[2]/div/p/text())").extract()
            # time = each.css(".bd_i_time_c::text").extract()
            # info = each.css(".bd_i_txt_c::text").extract()

            date = day + times[0]
            if self.is_first:
                item['date'] = date
                item['info'] = info[0]
                self.date_list.append(date)
                print(date + info[0])
            else:
                if date in self.date_list:
                    continue
                else:
                    item['date'] = date
                    item['info'] = info[0]
                    self.date_list.append(date)
                    print('-' * 60)
                    print(date + info[0])

            items.append(item)
        self.is_first = False
        # print('长度：%s' % len(items))
        return items  # 直接返回最后数据

    def closed(self, spider):
        self.log.info("sina7x24_spider_closed")
        self.driver.close()
