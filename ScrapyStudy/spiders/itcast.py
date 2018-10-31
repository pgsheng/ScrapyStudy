# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/10/30 15:09
"""
import scrapy

from ScrapyStudy.items import ItcastItem
from public.Log import Log


class ItcastSpider(scrapy.Spider):
    name = "itcast"  # 这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字
    allowed_domains = ["itcast.cn"]  # 搜索的域名范围，只爬取这个域名下的网页，不存在的URL会被忽略。
    # 爬取的URL元祖/列表。第一次下载数据将从这些urls开始。其他子URL将从这些URL中继承性生成。
    start_urls = [
        'http://www.itcast.cn/channel/teacher.shtml'
    ]

    def __init__(self):
        self.log = Log().get_logger()
        super(ItcastSpider, self).__init__()

    """
    解析的方法，每个初始URL完成下载后将被调用，调用时传入从每一个URL传回的Response对象来作为唯一参数，
    该方法作用:
    负责解析返回的网页数据(response.body)，提取结构化数据(生成item)，生成需要下一页的URL请求。
    """
    def parse(self, response):
        # 1、保存网页数据
        # filename = "teacher.html"
        # with open(filename, 'wb+') as file:  # 只能以二进制方式打开
        #     file.write(response.body)

        # context = response.xpath('/html/head/title/text()')
        # print(context.extract_first())         # 提取网站标题

        items = []          # 存放老师信息的集合

        for each in response.xpath("//div[@class='li_txt']"):
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = ItcastItem()
            # extract()方法返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            grade = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            # xpath返回的是包含一个元素的列表
            item['name'] = name[0].strip()
            item['grade'] = grade[0].strip()
            item['info'] = info[0].strip()

            items.append(item)

        # 直接返回最后数据
        return items