## 一、新建项目
    创建一个新的ScrapyStudy项目，进入项目目录，运行命令：
    scrapy startproject ScrapyStudy
    
    ```项目结构：
        scrapy.cfg: 项目的配置文件。
        ScrapyStudy/: 项目的Python模块，将会从这里引用代码。
        ScrapyStudy/items.py: 项目的目标文件。
        ScrapyStudy/pipelines.py: 项目的管道文件。
        ScrapyStudy/settings.py: 项目的设置文件。
        ScrapyStudy/spiders/: 存储爬虫代码目录。
    ```
## 二、明确目标(ScrapyStudy/items.py)
    Item定义结构化数据字段，用来保存爬取到的数据，有点像 Python 中的 dict，
    但是提供了一些额外的保护减少错误
    
## 三、制作爬虫 （spiders/itcast.py）
    创建一个类，并继承scrapy.Spider，并确定了三个强制的属性 和 一个方法:
    
    name = "itcast"  # 这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字
    allowed_domains = ["itcast.cn"]  # 搜索的域名范围，只爬取这个域名下的网页，不存在的URL会被忽略。
    # 爬取的URL元祖/列表。第一次下载数据将从这些urls开始。其他子URL将从这些URL中继承性生成。
    start_urls = [
        'http://www.itcast.cn/channel/teacher.shtml'
    ]
    
    parse(self, response)
    """
    解析的方法，每个初始URL完成下载后将被调用，调用时传入从每一个URL传回的Response对象来作为唯一参数，
    该方法作用:
    负责解析返回的网页数据(response.body)，提取结构化数据(生成item)，生成需要下一页的URL请求。
    """
    在此方法中做数据处理

## 四、保存数据 （pipelines.py）
     1、直接使用命令可以输出数据：-o 输出指定格式的文件
     "scrapy crawl itcast -o teachers.json" (-o teachers.csv 或 -o teachers.xml)
     2、在pipelines.py文件中定义数据输出,可输出为json、csv、xml等文件，亦可输出到数据库。
        pipelines定义后，需要在配置文件settings.py中添加激活才能使用：
            ITEM_PIPELINES = {
                #添加自己定义pipeline，300是优先级，有多个pipeline时优先级从低到高100、200、300顺序调用
                'ScrapyStudy.pipelines.Scrapystudy1Pipeline': 300，
            }



## 常见异常：
    1、UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 176: illegal multibyte sequence
       原因1：文件打开出现编码错误 ；原因2.  配置文件中 scrapy.cfg 含有中文字符