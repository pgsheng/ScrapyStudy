from scrapy.commands import ScrapyCommand
from scrapy.exceptions import UsageError
from scrapy.utils.conf import arglist_to_dict

from ScrapyStudy.public.Log import Log

"""
自定义scrapy命令的方式来同时运行多个爬虫
通过修改scrapy的crawl命令来完成同时执行spider的效果
并在设置文件setting中配置：COMMANDS_MODULE = 'ScrapyStudy.commands'  # 构建一个自定义项目命令
"""


class Command(ScrapyCommand):
    requires_project = True
    log = Log().get_logger()

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-a", dest="spargs", action="append", default=[], metavar="NAME=VALUE",
                          help="set spider argument (may be repeated)")
        parser.add_option("-o", "--output", metavar="FILE",
                          help="dump scraped items into FILE (use - for stdout)")
        parser.add_option("-t", "--output-format", metavar="FORMAT",
                          help="format to use for dumping items with -o")

    def process_options(self, args, opts):
        ScrapyCommand.process_options(self, args, opts)
        try:
            opts.spargs = arglist_to_dict(opts.spargs)
        except ValueError:
            raise UsageError("Invalid -a value, use -a NAME=VALUE", print_help=False)

    def run(self, args, opts):

        spider_loader = self.crawler_process.spider_loader
        for spider_name in args or spider_loader.list():
            self.log.info('准备爬取 %s' % spider_name)
            self.crawler_process.crawl(spider_name, **opts.spargs)

        self.crawler_process.start()
