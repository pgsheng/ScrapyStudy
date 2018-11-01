## 打包
    pyinstaller -F -i C:\AProjectCode\Python\ScrapyStudy\public\icon.ico C:\AProjectCode\Python\ScrapyStudy\main_run.py
    pyinstaller -F -i E:\PycharmProjects\ScrapyStudy\public\icon.ico E:\PycharmProjects\ScrapyStudy\main_run.py



## 常见异常：
    1、UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 176: illegal multibyte sequence
       原因1：文件打开出现编码错误 ；原因2.  配置文件中 scrapy.cfg 含有中文字符