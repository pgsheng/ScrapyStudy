# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

"""
明确你想要抓取的目标
"""


class ItcastItem(scrapy.Item):
    name = scrapy.Field()  # 定义类型为scrapy.Field的类属性来定义一个Item（可以理解成类似于ORM的映射关系）
    grade = scrapy.Field()
    info = scrapy.Field()


class JDItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    comment = scrapy.Field()
    product_id = scrapy.Field()


class Sina7x24Item(scrapy.Item):
    date = scrapy.Field()
    info = scrapy.Field()


class BeautyImageItem(scrapy.Item):
    image_url = scrapy.Field()
