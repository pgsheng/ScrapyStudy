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
    


## 常见异常：
   1、UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 176: illegal multibyte sequence
       原因1：文件打开出现编码错误 ；原因2.  配置文件中 scrapy.cfg 含有中文字符