"""
 @Author  : pgsheng
 @Time    : 2018/10/30 15:09
"""
import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from ScrapyStudy.items import Sina7x24Item
from ScrapyStudy.public import Config
from ScrapyStudy.public.Log import Log


class Sina7x24Spider(scrapy.Spider):
    name = "sina7x24"
    allowed_domains = ["finance.sina.com.cn"]
    start_urls = [
        'http://finance.sina.com.cn/7x24/'
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'ScrapyStudy.pipelines.Sina7x24Pipeline': 300, },
        'DOWNLOADER_MIDDLEWARES': {"ScrapyStudy.middlewares.SeleniumMiddleware": 401, }
    }

    def __init__(self):
        self.log = Log().get_logger()
        options = Options()  # 不同浏览器导入Options包路径不一样
        options.add_argument('-headless')  # 无界面配置
        self.driver = webdriver.Firefox(firefox_options=options)
        # self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
        super(Sina7x24Spider, self).__init__()

    def parse(self, response):
        filename = Config.get_results_path() + "sina7x24.html"  # 1、保存网页数据
        with open(filename, 'wb+') as file:  # 只能以二进制方式打开
            file.write(response.body)

        context = response.xpath('/html/head/title/text()')
        print(context.extract_first())  # 提取网站标题

        items = []
        news = response.xpath("//div[@class='bd_i bd_i_og  clearfix']")
        print(news)
        print(60 * '-')
        for each in news:
            item = Sina7x24Item()
            # extract()方法返回的都是unicode字符串,normalize-space()可以去掉数据中空格、换行符等特殊符号
            time = each.xpath("normalize-space(div/p/text())").extract()
            info = each.xpath("normalize-space(div[2]/div/p/text())").extract()
            print(time)
            print(info)
            item['time'] = time[0]
            item['info'] = info[0]

            items.append(item)

        return items  # 直接返回最后数据

    def closed(self, spider):
        self.log.info("spider closed")
        self.driver.close()
