## 打包命令：
    pyinstaller -F -i C:\AProjectCode\Python\ScrapyStudy\ScrapyStudy\public\icon.ico C:\AProjectCode\Python\ScrapyStudy\main_run.py
    pyinstaller -F -i E:\PycharmProjects\ScrapyStudy\ScrapyStudy\public\icon.ico E:\PycharmProjects\ScrapyStudy\main_run.py


## 打包后，运行exe保存系统依赖文件或数据文件找不到，解决方案：在site-packages/PyInstaller/hooks下构建
## scrapy-hook.py文件，输入以下内容保存，从新打包。
    #调用hook，批量导入数据与模块
    from PyInstaller.utils.hooks import collect_submodules, collect_data_files
    
    # This collects all dynamically imported scrapy modules and data files.
    # hiddenimports告诉pyinstaller有哪些隐形导入；datas告诉有哪些数据需要添加。
    hiddenimports = (collect_submodules('scrapy') +
                     collect_submodules('scrapy.pipelines') +
                     collect_submodules('scrapy.extensions') +
                     collect_submodules('scrapy.utils')+collect_submodules('scrapy.spiders')
    )
    #加载数据
    datas = collect_data_files('scrapy')


## 常见异常：
    1、UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 176: illegal multibyte sequence
       原因1：文件打开出现编码错误 ；原因2.  配置文件中 scrapy.cfg 含有中文字符
       
## 安装：
    pip install PyYAML # 读写yaml格式文件
    pip install Scrapy # 爬虫框架
    pip install pymongo # 数据库MongoDB操作
    pip install selenium # 浏览驱动框架
    pip install ./Twisted-18.9.0-cp36-cp36m-win_amd64.whl # python语言写的事件驱动的网络框架
    pip install ./pywin32-224-cp36-cp36m-win_amd64.whl # Python调用win
    pip install scrapy-splash # JS渲染服务
    splash服务需要依托docker，安装docker ：http://www.cnblogs.com/shaosks/p/6932319.html