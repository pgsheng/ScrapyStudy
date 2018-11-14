import os
import time

from scrapy import cmdline

from ScrapyStudy.public.Log import Log

log = Log().get_logger()

log.info(20 * '-' + '开始' + 20 * '-')
"""单个执行"""
cmdline.execute("scrapy crawl sina7x24".split())
# cmdline.execute("scrapy crawl itcast".split())  # 执行爬虫命令 不能去掉split()方法
# cmdline.execute("scrapy crawl jd".split()) #执行爬虫命令 不能去掉split()方法
# cmdline.execute("scrapy crawl itcast -o results//teachers0.json".split()) # -o 输出指定格式的文件
# cmdline.execute("scrapy crawl itcast -o results//teachers0.csv".split())
# cmdline.execute("scrapy crawl itcast -o results//teachers0.xml".split())

"""多个执行"""
# cmdline.execute("scrapy crawlall".split())


# if __name__ == '__main__':
#     while True:
#         os.system("scrapy crawl sina7x24")
#         # cmdline.execute("scrapy crawl sina7x24".split())
#         time.sleep(30)
