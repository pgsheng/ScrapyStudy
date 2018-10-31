# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

"""
设计管道存储爬取内容
"""

from scrapy.exporters import JsonLinesItemExporter

from public import Config
from public.Log import Log


class Scrapystudy1Pipeline(object):
    def __init__(self):
        self.log = Log().get_logger()
        filename = Config.get_results_path() + 'teachers.json'
        self.file = open(filename, 'wb')
        self.exporter = JsonLinesItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        # 当爬虫的数据返回时，这个方法被调用。
        # self.log.info(type(item))
        # line = json.dumps(dict(item)) + ",\n"
        # self.file.write(line)
        self.exporter.export_item(item)
        return item

    def open_spider(self, spider):
        # 可选实现，当spider被开启时，这个方法被调用。
        self.log.info('open_spider')

    def close_spier(self, spider):
        # 可选实现，当spider被关闭时，这个方法被调用,这里没有被调用，原因不详
        self.exporter.finish_exporting()
        self.file.close()


if __name__ == '__main__':
    Scrapystudy1Pipeline()
