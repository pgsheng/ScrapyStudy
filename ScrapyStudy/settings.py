# -*- coding: utf-8 -*-
"""
项目的设置文件
"""
# Scrapy settings for ScrapyStudy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ScrapyStudy'

SPIDER_MODULES = ['ScrapyStudy.spiders']
NEWSPIDER_MODULE = 'ScrapyStudy.spiders'

ROBOTSTXT_OBEY = True


FEED_EXPORT_ENCODING = 'utf-8'
