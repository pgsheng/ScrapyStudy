from scrapy import cmdline

"""单个执行"""
# cmdline.execute("scrapy crawl jd".split()) #执行爬虫命令 不能去掉split()方法
cmdline.execute("scrapy crawl itcast".split())  # 执行爬虫命令 不能去掉split()方法
# cmdline.execute("scrapy crawl itcast -o results//teachers0.json".split()) # -o 输出指定格式的文件
# cmdline.execute("scrapy crawl itcast -o results//teachers0.csv".split())
# cmdline.execute("scrapy crawl itcast -o results//teachers0.xml".split())

"""多个执行"""
cmdline.execute("scrapy crawlall".split())
