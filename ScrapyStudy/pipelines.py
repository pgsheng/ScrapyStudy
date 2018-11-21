# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

"""
设计管道存储爬取内容
"""
import pymongo
from scrapy import Request
from scrapy.exporters import JsonItemExporter
from scrapy.pipelines.images import ImagesPipeline

from ScrapyStudy.items import ItcastItem, Sina7x24Item
from ScrapyStudy.public import Config
from ScrapyStudy.public.Log import Log
from ScrapyStudy.spiders.MyExporters import MyCsvItemExporter


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
        fields = ['name', 'grade', 'info']
        self.csv_exporter = MyCsvItemExporter(fields=fields, file=self.csv_file, encoding='utf-8')

        """存储数据库"""
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client['scrapydb']  # 指定数据库
        self.collection = db['teachers']  # 指定集合

    def process_item(self, item, spider):
        # 当爬虫的数据返回时，这个方法被调用。
        if isinstance(item, ItcastItem):
            # line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
            # self.file.writelines(line)
            self.exporter.export_item(item)
            self.csv_exporter.export_item(item)
            # result = self.collection.insert_one(dict(item))
            # self.log.info(result.inserted_id)
        return item

    def open_spider(self, spider):
        # 可选实现，当spider被开启时，这个方法被调用。
        self.log.info('open_itcast_spider')

    def close_spider(self, spider):
        # 可选实现，当spider被关闭时，这个方法被调用,这里没有被调用，原因不详
        self.exporter.finish_exporting()
        self.file.close()
        self.csv_file.close()
        self.log.info('close_itcast_spider')


class JDPipeline(object):
    def __init__(self):
        self.log = Log().get_logger()
        """输出json,使用内置JsonItemExporter实现，或自己使用内置json实现"""
        filename = Config.get_results_path() + 'jd.json'
        self.file = open(filename, 'wb')
        self.exporter = JsonItemExporter(self.file, indent=0, encoding='utf-8')
        self.exporter.start_exporting()

        """输出csv,使用自定义MyCsvItemExporter可指定顺序和分隔符"""
        csv_filename = Config.get_results_path() + 'jd.csv'
        self.csv_file = open(csv_filename, 'wb')
        fields = ['title', 'price', 'comment', 'product_id']
        self.csv_exporter = MyCsvItemExporter(fields=fields, file=self.csv_file, encoding='gbk')

    def process_item(self, item, spider):
        # 当爬虫的数据返回时，这个方法被调用。
        self.log.info('这是京东网站数据')

        self.exporter.export_item(item)
        self.csv_exporter.export_item(item)
        return item

    def open_spider(self, spider):
        # 可选实现，当spider被开启时，这个方法被调用。
        self.log.info('open_jd_spider')

    def close_spider(self, spider):
        # 可选实现，当spider被关闭时，这个方法被调用,这里没有被调用，原因不详
        self.exporter.finish_exporting()
        self.file.close()
        self.log.info('close_jd_spider')


class Sina7x24Pipeline(object):
    def __init__(self):
        self.log = Log().get_logger()
        """输出json,使用内置JsonItemExporter实现，或自己使用内置json实现"""
        filename = Config.get_results_path() + 'sina7x24.json'
        self.file = open(filename, 'wb')
        self.exporter = JsonItemExporter(self.file, indent=0, encoding='utf-8')
        # self.exporter = MyJsonLinesItemExporter(self.file, indent=0, encoding='utf-8')
        self.exporter.start_exporting()

        """存储数据库"""
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client['sinadb']  # 指定数据库
        self.collection = db['7x24']  # 指定集合

    def process_item(self, item, spider):
        # 当爬虫的数据返回时，这个方法被调用。
        if isinstance(item, Sina7x24Item):
            self.exporter.export_item(item)

            myquery = {"date": item['date']}
            newvalues = {"$set": dict(item)}
            result = self.collection.update_many(myquery, newvalues, upsert=True)
            # self.log.info('插入数据id：%s' % result.upserted_id)
        return item

    def open_spider(self, spider):
        # 可选实现，当spider被开启时，这个方法被调用。
        self.log.info('open_sina7x24_spider')

    def close_spider(self, spider):
        # 可选实现，当spider被关闭时，这个方法被调用,这里没有被调用，原因不详
        self.exporter.finish_exporting()
        self.file.close()
        self.log.info('close_sina7x24_spider')


#  图片下载,继承ImagesPipeline
class BeautyImagePipeline(ImagesPipeline):
    log = Log().get_logger()

    def get_media_requests(self, item, info):
        for image_url in item['image_url']:
            self.log.info(image_url)
            yield Request(image_url)

    # def file_path(self, request, response=None, info=None):
    #     item = request.meta['item']  # 通过上面的meta传递过来item
    #     index = request.meta['index']  # 通过上面的index传递过来列表中当前下载图片的下标
    #
    #     # 图片文件名，item['carname'][index]得到汽车名称，request.url.split('/')[-1].split('.')[-1]得到图片后缀jpg,png
    #     image_guid = item['carname'][index] + '.' + request.url.split('/')[-1].split('.')[-1]
    #     # 图片下载目录 此处item['country']即需要前面item['country']=''.join()......,否则目录名会变成\u97e9\u56fd\u6c7d\u8f66\u6807\u5fd7\xxx.jpg
    #     filename = u'full/{0}/{1}'.format(item['country'], image_guid)
    #     return filename


"""
    注意:get_media_requests()方法不能和一下方法共存
    def open_spider(self, spider):
        # 可选实现，当spider被开启时，这个方法被调用。
        self.log.info('open_beautyimage_spider')

    def process_item(self, item, spider):
        return item
"""
