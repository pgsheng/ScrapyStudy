# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

"""
设计管道存储爬取内容
"""

from scrapy.exporters import JsonItemExporter

from ScrapyStudy.items import JDItem, ItcastItem
from ScrapyStudy.spiders.MyCsvItemExporter import MyCsvItemExporter
from public import Config
from public.Log import Log


class ItcastPipeline(object):
    def __init__(self):
        self.log = Log().get_logger()
        """输出json,使用内置JsonItemExporter实现，或自己使用内置json实现"""
        filename = Config.get_results_path() + 'teachers.json'
        # self.file = open(filename, 'w' , encoding='utf-8')
        self.file = open(filename, 'wb')
        self.exporter = JsonItemExporter(self.file, indent=0, encoding='utf-8')
        self.exporter.start_exporting()

        """输出csv,使用自定义MyCsvItemExporter可指定顺序和分隔符"""
        csv_filename = Config.get_results_path() + 'teachers.csv'
        self.csv_file = open(csv_filename, 'wb')
        self.csv_exporter = MyCsvItemExporter(self.csv_file, encoding='gbk')

    def process_item(self, item, spider):
        # 当爬虫的数据返回时，这个方法被调用。
        # line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        # self.file.writelines(line)
        self.exporter.export_item(item)
        self.csv_exporter.export_item(item)
        return item

    def open_spider(self, spider):
        # 可选实现，当spider被开启时，这个方法被调用。
        self.log.info('open_spider')

    def close_spider(self, spider):
        # 可选实现，当spider被关闭时，这个方法被调用,这里没有被调用，原因不详
        self.exporter.finish_exporting()
        self.file.close()
        self.log.info('close_spider')


class JDPipeline(object):
    def __init__(self):
        self.log = Log().get_logger()
        """输出json,使用内置JsonItemExporter实现，或自己使用内置json实现"""
        filename = Config.get_results_path() + 'jd.json'
        self.file = open(filename, 'wb')
        self.exporter = JsonItemExporter(self.file, indent=0, encoding='utf-8')
        self.exporter.start_exporting()

        """输出csv,使用自定义MyCsvItemExporter可指定顺序和分隔符"""
        csv_filename = Config.get_results_path() + 'teachers.csv'
        self.csv_file = open(csv_filename, 'wb')
        self.csv_exporter = MyCsvItemExporter(self.csv_file, encoding='gbk')

    def process_item(self, item, spider):
        # 当爬虫的数据返回时，这个方法被调用。
        self.log.info('这是京东网站数据')

        self.exporter.export_item(item)
        self.csv_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 可选实现，当spider被关闭时，这个方法被调用,这里没有被调用，原因不详
        self.exporter.finish_exporting()
        self.file.close()
        self.log.info('close_spider')