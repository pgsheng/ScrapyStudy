from scrapy import cmdline

cmdline.execute("scrapy crawl itcast".split()) #执行爬虫命令 不能去掉split()方法
# cmdline.execute("scrapy crawl itcast -o results//teachers0.json".split()) # -o 输出指定格式的文件
# cmdline.execute("scrapy crawl itcast -o results//teachers0.csv".split())
# cmdline.execute("scrapy crawl itcast -o results//teachers0.xml".split())
