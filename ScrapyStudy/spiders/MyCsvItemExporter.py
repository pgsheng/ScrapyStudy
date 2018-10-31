# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/10/31 15:35
"""
from scrapy.exporters import CsvItemExporter


class MyCsvItemExporter(CsvItemExporter):
    """Scrapy抓取数据输出到CSV文件，CsvItemExporter不是按照items.py中定义的字段的顺序"""

    def __init__(self, *args, **kwargs):
        # delimiter = settings.get('CSV_DELIMITER', '\t')  # 指定csv文件中的分隔符
        # kwargs['delimiter'] = delimiter
        kwargs['delimiter'] = ','

        # 指定自定csv输出字段及顺序
        # fields_to_export = settings.get('FIELDS_TO_EXPORT', []) # 设置文件settings设置也可以
        fields_to_export = ['name', 'grade', 'info']
        if fields_to_export:
            kwargs['fields_to_export'] = fields_to_export

        super(MyCsvItemExporter, self).__init__(*args, **kwargs)
