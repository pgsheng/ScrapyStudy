"""
项目的设置文件
"""
BOT_NAME = 'ScrapyStudy'  # 爬虫项目的名字

SPIDER_MODULES = ['ScrapyStudy.spiders']  # 爬虫的路径
NEWSPIDER_MODULE = 'ScrapyStudy.spiders'  # 爬虫的路径

# ITEM_PIPELINES = {
#     # 添加自己定义pipeline，300是优先级，有多个pipeline时优先级从低到高100、200、300顺序调用
#     # 注意：这里定义所有爬虫spiders共有的pipeline，需在pipeline做数据类型判断再做对应数据保存处理
#     # 其他方案：直接在spiders指定对应 pipeline，就不需要做数据类型判断
#     'ScrapyStudy.pipelines.ItcastPipeline': 300,
# }

# DOWNLOADER_MIDDLEWARES = { # 下载中间件，可以自定义
#     "Sina_spider1.middleware.UserAgentMiddleware": 401,
#     "Sina_spider1.middleware.CookiesMiddleware": 402,
# }

# 请求头，用来表示请求者的信息，比如会带着客户端的爬虫名称去访问爬虫网站，如果被识别到就会被拒绝，
# 因此可以参考反爬虫的博文，动态伪装成浏览器，以便成功爬取
# USER_AGENT = ''
# 并发请求数，最大是32，写成2，代表一次发2个。如果对方没有做反爬虫机制，可很大并发，可以一下返回很多数据。
# CONCURRENT_REQUESTS = 2

COMMANDS_MODULE = 'ScrapyStudy.commands'  # 构建一个自定义项目命令
DOWNLOAD_DELAY = 2  # 下载延迟秒数，限制频繁访问，以防止被封号

# LOG_FILE = "mySpider.log" # 输出log文件
LOG_LEVEL = "DEBUG"  # logging级别，DEBUG 、INFO、WARNING 、ERROR 、CRITICAL
LOG_ENABLED = True  # True启用logging，默认,True，False
LOG_ENCODING = 'utf-8'  # logging使用的编码

FEED_EXPORT_ENCODING = 'utf-8'  # 配置编码

ROBOTSTXT_OBEY = False  # True遵守robots.txt的规则。False拒绝遵守Robot协议。
# Robot协议保存在网站的服务器中，作用是告诉本网站哪些目录下的网页不希望你进行爬取收录

# FEED_EXPORTERS = {
#     'csv': 'ScrapyStudy.spiders.MyCsvItemExporter.MyCsvItemExporter',  # 指定自定义输出csv格式类
# }
#
# FIELDS_TO_EXPORT = [  # 指定自定csv输出字段及顺序
#     'name',
#     'grade',
#     'info'
# ]
