"""
 @Author  : pgsheng
 @Time    : 2018/10/31 15:35
"""
from scrapy.exporters import CsvItemExporter


class MyCsvItemExporter(CsvItemExporter):
    """Scrapy抓取数据输出到CSV文件，CsvItemExporter不是按照items.py中定义的字段的顺序"""

    def __init__(self, fields=list(), delimiter='\t', *args, **kwargs):
        # delimiter = settings.get('CSV_DELIMITER', '\t')   # 从设置文件配置
        # kwargs['delimiter'] = delimiter
        kwargs['delimiter'] = delimiter  # 指定csv文件中的分隔符

        # 指定自定csv输出字段及顺序
        # fields = settings.get('FIELDS_TO_EXPORT', []) # 设置文件settings设置也可以
        # fields = ['name', 'grade', 'info']
        if fields:
            kwargs['fields_to_export'] = fields

        super(MyCsvItemExporter, self).__init__(*args, **kwargs)
